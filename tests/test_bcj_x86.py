import pathlib

import bcj


def test_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    result = bcj.x86_decode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(result)


def test_simple_x86_decode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86.bin'), 'rb') as f:
        src = f.read()
    result = bcj.simple_x86_decode(src)
    with open(tmp_path.joinpath('output.bin'), 'wb') as f:
        f.write(result)
