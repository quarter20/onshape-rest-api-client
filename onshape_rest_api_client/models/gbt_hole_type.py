from enum import StrEnum


class GBTHoleType(StrEnum):
    C_BORE = "C_BORE"
    C_SINK = "C_SINK"
    SIMPLE = "SIMPLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
