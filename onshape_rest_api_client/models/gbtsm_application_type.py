from enum import StrEnum


class GBTSMApplicationType(StrEnum):
    FLEXIBLE_PCB = "FLEXIBLE_PCB"
    NONE = "NONE"
    SHEET_METAL = "SHEET_METAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
