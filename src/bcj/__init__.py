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

from bcj._x86 import ffi, lib as bcj_x86

BUFFER_LENGTH = 8192


class Encoder:

    def __init__(self):
        self.simple = ffi.new('simple_x86*')
        bcj_x86.bcj_x86_simple_x86_init

    def x86_encode(self, inbuf: bytes):
        out_remaining = len(inbuf)
        buf = ffi.from_buffer(inbuf)
        pos = 0
        while out_remaining > 0:
            max_length = min(BUFFER_LENGTH, out_remaining)
            size = bcj_x86.bcj_x86_encoder(self.simple, buf, pos, max_length)
            if size == 0:
                break
            out_remaining -= size
            pos += size
        out = ffi.buffer(buf)
        return out


class Decoder:
    def __init__(self):
        self.simple = ffi.new('simple_x86*')
        bcj_x86.bcj_x86_simple_x86_init

    def x86_decode(self, inbuf: bytes):
        out_remaining = len(inbuf)
        buf = ffi.from_buffer(inbuf)
        pos = 0
        while out_remaining > 0:
            max_length = min(BUFFER_LENGTH, out_remaining)
            size = bcj_x86.bcj_x86_decoder(self.simple, buf, pos, max_length)
            if size == 0:
                break
            out_remaining -= size
            pos += size
        out = ffi.buffer(buf)
        return out
