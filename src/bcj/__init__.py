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


class BCJFilter:

    def __init__(self, func, is_encoder: bool):
        self.is_encoder = is_encoder
        self.buffer = bytearray()
        self.state = ffi.new('UInt32 *', 0)
        self.method = func
        self.ip = 0

    def _x86_code(self):
        size = len(self.buffer)
        buf = ffi.from_buffer(self.buffer, require_writable=True)
        if self.is_encoder:
            out_size = lib.x86_Convert(buf, size, self.ip, self.state, 1)
        else:
            out_size = lib.x86_Convert(buf, size, self.ip, self.state, 0)
        result = ffi.buffer(buf)[:out_size]
        self.ip += out_size
        self.buffer = self.buffer[out_size:]
        return result

    def _decode(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        self.buffer.extend(data)
        return self.method()

    def _encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        self.buffer.extend(data)
        return self.method()

    def _flush(self):
        return bytes(self.buffer)


class BCJDecoder(BCJFilter):

    def __init__(self, size: int):
        super().__init__(self._x86_code, False)
        self.stream_size = size

    def decode(self, data: Union[bytes, bytearray, memoryview], max_length: int = -1) -> bytes:
        if self.ip >= self.stream_size:
            return b''
        result = self._decode(data)
        if self.ip > self.stream_size - 5:
            result += self.buffer[-5:]
            self.ip += 5
        return result


class BCJEncoder(BCJFilter):

    def __init__(self):
        super().__init__(self._x86_code, True)

    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes:
        return self._encode(data)

    def flush(self):
        return self._flush()
