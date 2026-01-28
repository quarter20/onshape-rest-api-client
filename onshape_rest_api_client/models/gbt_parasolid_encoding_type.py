from enum import Enum


class GBTParasolidEncodingType(str, Enum):
    BINARY = "BINARY"
    TEXT = "TEXT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
