from enum import StrEnum


class GBTComputeStatus(StrEnum):
    COMPUTED = "COMPUTED"
    COMPUTING = "COMPUTING"
    ERROR = "ERROR"
    PREPARING = "PREPARING"
    STALE = "STALE"
    UNDERDEFINED = "UNDERDEFINED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
