import binascii
import pathlib
import hashlib

import bcj


def test_x86_encode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    encoder = bcj.Encoder()
    dest, size = encoder.x86_encode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256()
    m.update(dest)
    assert size == origin
    assert m.digest() == binascii.unhexlify('6563f2cb8b3f4f754793ee8df9b1617aeca4ed4b6753549e65c4809141b2f6fd')



def test_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/bcj.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    decoder = bcj.Decoder()
    dest, size = decoder.x86_decode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256()
    m.update(dest)
    assert size == origin
    assert m.digest() == binascii.unhexlify('0e989ba003598803f58708e588640e323e2345eced5518abba78adf909c35b3b')
