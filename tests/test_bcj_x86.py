import pathlib

import bcj

def test_encode(tmp_path):
    with open(pathlib.Path(__file__).parent.joinpath('data/x86binary'), 'rb') as f:
        src = f.read()
    result = bcj.bcj_x86_decode(src)
    with open(tmp_path.joinpath('output'), 'wb') as f:
        f.write(result)
