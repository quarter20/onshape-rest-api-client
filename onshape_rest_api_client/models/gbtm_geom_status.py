from enum import Enum


class GBTMGeomStatus(str, Enum):
    FIXED = "FIXED"
    NOT_CONSISTENT = "NOT_CONSISTENT"
    OVER_DEFINED = "OVER_DEFINED"
    UNDER_DEFINED = "UNDER_DEFINED"
    UNKNOWN = "UNKNOWN"
    WELL_DEFINED = "WELL_DEFINED"

    def __str__(self) -> str:
        return str(self.value)
