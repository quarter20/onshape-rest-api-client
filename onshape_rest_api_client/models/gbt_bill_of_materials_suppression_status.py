from enum import StrEnum


class GBTBillOfMaterialsSuppressionStatus(StrEnum):
    SUPPRESSED = "SUPPRESSED"
    UNKNOWN = "UNKNOWN"
    UNSET = "UNSET"
    UNSUPPRESSED = "UNSUPPRESSED"

    def __str__(self) -> str:
        return str(self.value)
