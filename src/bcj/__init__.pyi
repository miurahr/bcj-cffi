#from _bcj import ffi as ffi, lib as lib
from typing import Any, Union

class BCJFilter:
    is_encoder: Any = ...
    buffer: Any = ...
    state: Any = ...
    ip: int = ...
    stream_size: Any = ...
    method: Any = ...
    def __init__(self, func: Any, readahead: int, is_encoder: bool, stream_size: int=...) -> None: ...

class BCJDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...
    def decode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...

class BCJEncoder(BCJFilter):
    def __init__(self) -> None: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...

class SparcDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...
    def decode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...

class SparcEncoder(BCJFilter):
    def __init__(self) -> None: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...

class PpcDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...
    def decode(self, data: Union[bytes, bytearray, memoryview], max_length: int=...) -> bytes: ...

class PpcEncoder(BCJFilter):
    def __init__(self) -> None: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...

class ArmtDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...
    def decode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...

class ArmtEncoder(BCJFilter):
    def __init__(self) -> None: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...

class ArmDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...
    def decode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...

class ArmEncoder(BCJFilter):
    def __init__(self) -> None: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...