from enum import StrEnum


class GBTStlEncodingType(StrEnum):
    BINARY = "BINARY"
    TEXT = "TEXT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
