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

BUFFER_LENGTH = 4096


def simple_x86_decode(inbuf: bytes):
    size = len(inbuf)
    buf = ffi.from_buffer(inbuf)
    out_size = bcj_x86.simple_bcj_x86_decoder(buf, size)
    return ffi.buffer(buf), out_size


class Encoder:

    def __init__(self):
        self.simple = ffi.new('simple_x86*')
        bcj_x86.bcj_x86_simple_x86_init

    def x86_encode(self, inbuf: bytes):
        out_remaining = len(inbuf)
        out_size = 0
        dest = b''
        while out_remaining > 0:
            max_length = min(BUFFER_LENGTH, out_remaining, len(inbuf))
            indata = inbuf[:max_length]
            out, size = self._x86_encode(indata)
            out_remaining = out_remaining - size
            out_size += size
            dest = dest + out
            if max_length == len(inbuf):
                break
            inbuf = inbuf[size:]
        return dest, out_size

    def _x86_encode(self, inbuf: bytes):
        size = len(inbuf)
        buf = ffi.from_buffer(inbuf)
        out_size = bcj_x86.bcj_x86_encoder(self.simple, buf, size)
        result = ffi.buffer(buf)
        return result[:out_size], out_size


class Decoder:
    def __init__(self):
        self.simple = ffi.new('simple_x86*')
        bcj_x86.bcj_x86_simple_x86_init

    def x86_decode(self, inbuf: bytes):
        out_remaining = len(inbuf)
        out_size = 0
        dest = b''
        while out_remaining > 0:
            max_length = min(BUFFER_LENGTH, out_remaining, len(inbuf))
            indata = inbuf[:max_length]
            out, size = self._x86_decode(indata)
            out_remaining = out_remaining - size
            out_size += size
            dest = dest + out
            if max_length == len(inbuf):
                break
            inbuf = inbuf[size:]
        return dest, out_size

    def _x86_decode(self, inbuf: bytes):
        size = len(inbuf)
        buf = ffi.from_buffer(inbuf)
        out_size = bcj_x86.bcj_x86_decoder(self.simple, buf, size)
        result = ffi.buffer(buf)
        return result[:out_size], out_size
