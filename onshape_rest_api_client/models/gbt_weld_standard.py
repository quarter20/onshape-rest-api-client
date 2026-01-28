from enum import Enum


class GBTWeldStandard(str, Enum):
    ANSI = "ANSI"
    ISO = "ISO"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
