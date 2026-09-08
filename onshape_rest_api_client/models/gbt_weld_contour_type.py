from enum import StrEnum


class GBTWeldContourType(StrEnum):
    CONCAVE = "CONCAVE"
    CONVEX = "CONVEX"
    FLAT = "FLAT"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
