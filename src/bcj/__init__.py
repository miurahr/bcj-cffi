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


def bcj_x86_decode(inbuf: bytes):
    size = len(inbuf)
    buf = ffi.from_buffer(inbuf)
    out_size = bcj_x86.simple_bcj_x86_decoder(buf, size)
    return ffi.buffer(buf)
