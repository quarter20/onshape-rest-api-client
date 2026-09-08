from enum import StrEnum


class GBTMGeomStatus(StrEnum):
    FIXED = "FIXED"
    NOT_CONSISTENT = "NOT_CONSISTENT"
    OVER_DEFINED = "OVER_DEFINED"
    UNDER_DEFINED = "UNDER_DEFINED"
    UNKNOWN = "UNKNOWN"
    WELL_DEFINED = "WELL_DEFINED"

    def __str__(self) -> str:
        return str(self.value)
