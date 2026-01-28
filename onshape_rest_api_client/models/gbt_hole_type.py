from enum import Enum


class GBTHoleType(str, Enum):
    C_BORE = "C_BORE"
    C_SINK = "C_SINK"
    SIMPLE = "SIMPLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
