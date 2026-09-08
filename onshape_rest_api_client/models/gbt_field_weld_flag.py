from enum import StrEnum


class GBTFieldWeldFlag(StrEnum):
    LOWER = "LOWER"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"
    UPPER = "UPPER"

    def __str__(self) -> str:
        return str(self.value)
