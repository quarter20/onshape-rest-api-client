from enum import StrEnum


class GBTWeldStandard(StrEnum):
    ANSI = "ANSI"
    ISO = "ISO"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
