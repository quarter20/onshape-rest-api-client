from enum import Enum


class GBTSMApplicationType(str, Enum):
    FLEXIBLE_PCB = "FLEXIBLE_PCB"
    NONE = "NONE"
    SHEET_METAL = "SHEET_METAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
