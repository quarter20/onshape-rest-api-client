from enum import Enum


class GBTTableTextAlignment(str, Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
