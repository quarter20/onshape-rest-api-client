from enum import Enum


class GBTGraphicsBufferTarget(str, Enum):
    ARRAY_BUFFER = "ARRAY_BUFFER"
    ELEMENT_ARRAY_BUFFER = "ELEMENT_ARRAY_BUFFER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
