import binascii
import pathlib
import hashlib

import bcj


def test_x86_encode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    encoder = bcj.Encoder()
    dest = encoder.x86_encode(src)
    size = len(dest)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256(dest)
    assert size == origin
    assert m.digest() == binascii.unhexlify('e396dadbbe0be4190cdea986e0ec949b049ded2b38df19268a78d32b90b72d42')


def test_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/bcj.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    decoder = bcj.Decoder()
    dest = decoder.x86_decode(src)
    size = len(dest)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256(dest)
    assert size == origin
    assert m.digest() == binascii.unhexlify('5ae0726746e2ccdad8f511ecfcf5f79df4533b83f86b1877cebc07f14a4e9b6a')
