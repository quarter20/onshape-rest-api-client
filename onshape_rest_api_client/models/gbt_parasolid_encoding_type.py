from enum import StrEnum


class GBTParasolidEncodingType(StrEnum):
    BINARY = "BINARY"
    TEXT = "TEXT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
