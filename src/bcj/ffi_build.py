import cffi
import pathlib


ffibuilder = cffi.FFI()

ffibuilder.cdef(r'''
typedef struct {
	uint32_t prev_mask;
	uint32_t prev_pos;
} simple_x86;
''')
ffibuilder.cdef('void bcj_x86_simple_x86_init(simple_x86*);')
ffibuilder.cdef('size_t bcj_x86_encoder(simple_x86*, uint8_t*, size_t);')
ffibuilder.cdef('size_t bcj_x86_decoder(simple_x86*, uint8_t*, size_t);')

ffibuilder.set_source('bcj._x86', r'''
typedef struct {
	uint32_t prev_mask;
	uint32_t prev_pos;
} simple_x86;
''', sources=[pathlib.Path(__file__).parent.parent.joinpath('xz_bcj_x86.c').as_posix()])


if __name__ == "__main__":    # not when running with setuptools
    ffibuilder.compile(verbose=True)
