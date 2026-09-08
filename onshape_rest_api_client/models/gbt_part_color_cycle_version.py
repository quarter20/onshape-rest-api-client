from enum import StrEnum


class GBTPartColorCycleVersion(StrEnum):
    COLOR_CYCLE_0 = "COLOR_CYCLE_0"
    COLOR_CYCLE_1 = "COLOR_CYCLE_1"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
