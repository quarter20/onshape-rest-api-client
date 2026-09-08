from enum import StrEnum


class GBTTableColumnWidthUnits(StrEnum):
    CHARS = "CHARS"
    PERCENT = "PERCENT"
    PIXELS = "PIXELS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
