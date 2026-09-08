from enum import StrEnum


class GBTTableTextAlignment(StrEnum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
