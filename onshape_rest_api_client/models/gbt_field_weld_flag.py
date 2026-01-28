from enum import Enum


class GBTFieldWeldFlag(str, Enum):
    LOWER = "LOWER"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"
    UPPER = "UPPER"

    def __str__(self) -> str:
        return str(self.value)
