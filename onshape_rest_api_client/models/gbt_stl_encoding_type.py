from enum import Enum


class GBTStlEncodingType(str, Enum):
    BINARY = "BINARY"
    TEXT = "TEXT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
