import binascii
import pathlib
import hashlib

import bcj


def test_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    dest, size = bcj.x86_decode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256()
    m.update(dest)
    assert m.digest() == binascii.unhexlify('3c571b444bd6ea451a260e6529939d66efbb077e6b6a38f36c0e1b69cac1a622')
    assert size == origin


def test_simple_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    origin = len(src)
    dest, size = bcj.simple_x86_decode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(dest)
    m = hashlib.sha256()
    m.update(dest)
    assert m.digest() == binascii.unhexlify('3c571b444bd6ea451a260e6529939d66efbb077e6b6a38f36c0e1b69cac1a622')
    assert size == origin
