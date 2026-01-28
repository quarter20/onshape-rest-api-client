from enum import Enum


class GBTPartColorCycleVersion(str, Enum):
    COLOR_CYCLE_0 = "COLOR_CYCLE_0"
    COLOR_CYCLE_1 = "COLOR_CYCLE_1"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
