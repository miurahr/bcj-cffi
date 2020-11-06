import cffi
import pathlib

ext_dir = pathlib.Path(__file__).parent.parent
sources = [ext_dir.joinpath(s).as_posix() for s in ['Bcj2.c', 'Bra.c', 'Bra86.c', 'BraIA64.c']]

ffibuilder = cffi.FFI()


# 7zTypes.h
ffibuilder.cdef(r'''
typedef unsigned char Byte;
typedef unsigned short UInt16;
typedef unsigned int UInt32;
typedef unsigned long long UInt64;
typedef size_t SizeT;
''')

# Bcj.h
ffibuilder.cdef(r'''
SizeT x86_Convert(Byte *data, SizeT size, UInt32 ip, UInt32 *state, int encoding);
SizeT ARM_Convert(Byte *data, SizeT size, UInt32 ip, int encoding);
SizeT ARMT_Convert(Byte *data, SizeT size, UInt32 ip, int encoding);
SizeT PPC_Convert(Byte *data, SizeT size, UInt32 ip, int encoding);
SizeT SPARC_Convert(Byte *data, SizeT size, UInt32 ip, int encoding);
SizeT IA64_Convert(Byte *data, SizeT size, UInt32 ip, int encoding);
''')

# Bcj2.h
ffibuilder.cdef(r'''
typedef enum
{
  BCJ2_ENC_FINISH_MODE_CONTINUE,
  BCJ2_ENC_FINISH_MODE_END_BLOCK,
  BCJ2_ENC_FINISH_MODE_END_STREAM
} EBcj2Enc_FinishMode;

typedef struct
{
  Byte *bufs[BCJ2_NUM_STREAMS];
  const Byte *lims[BCJ2_NUM_STREAMS];
  const Byte *src;
  const Byte *srcLim;
  unsigned state;
  EBcj2Enc_FinishMode finishMode;
  Byte prevByte;
  Byte cache;
  UInt32 range;
  UInt64 low;
  UInt64 cacheSize;
  UInt32 ip;
  UInt32 fileIp;
  UInt32 fileSize;
  UInt32 relatLimit;
  UInt32 tempTarget;
  unsigned tempPos;
  Byte temp[4 * 2];
  unsigned flushPos;
  UInt16 probs[2 + 256];
} CBcj2Enc;
void Bcj2Enc_Init(CBcj2Enc *p);
void Bcj2Enc_Encode(CBcj2Enc *p);
''')

ffibuilder.set_source('_bcj', None, sources=sources)


if __name__ == "__main__":    # not when running with setuptools
    ffibuilder.compile(verbose=True)
