from enum import Enum


class GBTTableColumnWidthUnits(str, Enum):
    CHARS = "CHARS"
    PERCENT = "PERCENT"
    PIXELS = "PIXELS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
