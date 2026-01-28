from enum import Enum


class GBTToleranceType(str, Enum):
    BASIC = "BASIC"
    DEFAULT = "DEFAULT"
    DEVIATION = "DEVIATION"
    FIT = "FIT"
    FIT_TOLERANCE_ONLY = "FIT_TOLERANCE_ONLY"
    FIT_WITH_TOLERANCE = "FIT_WITH_TOLERANCE"
    LIMITS = "LIMITS"
    MAX = "MAX"
    MIN = "MIN"
    NONE = "NONE"
    SYMMETRICAL = "SYMMETRICAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
