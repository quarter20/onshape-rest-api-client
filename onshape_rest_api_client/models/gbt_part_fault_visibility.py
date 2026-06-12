from enum import Enum


class GBTPartFaultVisibility(str, Enum):
    HIDDEN = "HIDDEN"
    UNKNOWN = "UNKNOWN"
    UNSPECIFIED = "UNSPECIFIED"
    VISIBLE = "VISIBLE"

    def __str__(self) -> str:
        return str(self.value)
