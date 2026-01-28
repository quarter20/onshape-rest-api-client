from enum import Enum


class GBTEntityEdgeSmoothnessStatus(str, Enum):
    NOT_SMOOTH = "NOT_SMOOTH"
    SMOOTH = "SMOOTH"
    SMOOTH_V2 = "SMOOTH_V2"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
