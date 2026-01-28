from enum import Enum


class GBTBillOfMaterialsSuppressionStatus(str, Enum):
    SUPPRESSED = "SUPPRESSED"
    UNKNOWN = "UNKNOWN"
    UNSET = "UNSET"
    UNSUPPRESSED = "UNSUPPRESSED"

    def __str__(self) -> str:
        return str(self.value)
