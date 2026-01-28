from enum import Enum


class GBTPatternType(str, Enum):
    CIRCULAR = "CIRCULAR"
    LINEAR = "LINEAR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
