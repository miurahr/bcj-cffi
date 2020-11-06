from typing import Union

try:
    from importlib.metadata import PackageNotFoundError, version  # type: ignore
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore

__copyright__ = 'Copyright (C) 2020 Hiroshi Miura'

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no-cover
    # package is not installed
    __version__ = "unknown"

from _bcj import ffi, lib

BUFFER_LENGTH = 4096


class BCJFilter:

    def __init__(self, func, is_encoder: bool, size: int):
        self.is_encoder = is_encoder
        self.buffer = bytearray()
        self.state = 0
        self.method = func
        self.stream_size = size
        self.ip = 0

    def _x86_code(self):
        size = len(self.buffer)
        ip = 0
        buf = ffi.from_buffer(self.buffer)
        if self.is_encoder:
            out_size = lib.x86_Convert(buf, size, self.ip, self.state, 1)
        else:
            out_size = lib.x86_Convert(buf, size, self.ip, self.state, 0)
        result = ffi.buffer(buf)
        return result[:out_size], out_size

    def _decompress(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        self.buffer.extend(data)
        result, pos = self._method()
        self.buffer = self.buffer[pos:]
        return result

    def _compress(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        self.buffer.extend(data)
        result, pos = self._method()
        self.buffer = self.buffer[pos:]
        return result

    def _flush(self):
        return bytes(self.buffer)


class BCJDecoder(BCJFilter):

    def __init__(self, size: int):
        super().__init__(self._x86_code, False, size)

    def decompress(self, data: Union[bytes, bytearray, memoryview], max_length: int = -1) -> bytes:
        return self._decompress(data)


class BCJEncoder(BCJFilter):

    def __init__(self):
        super().__init__(self._x86_code, True)

    def compress(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        return self._compress(data)

    def flush(self):
        return self._flush()
