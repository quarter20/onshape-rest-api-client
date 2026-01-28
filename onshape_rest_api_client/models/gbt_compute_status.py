from enum import Enum


class GBTComputeStatus(str, Enum):
    COMPUTED = "COMPUTED"
    COMPUTING = "COMPUTING"
    ERROR = "ERROR"
    PREPARING = "PREPARING"
    STALE = "STALE"
    UNDERDEFINED = "UNDERDEFINED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
