from enum import Enum


class GBTWeldContourType(str, Enum):
    CONCAVE = "CONCAVE"
    CONVEX = "CONVEX"
    FLAT = "FLAT"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
