from enum import Enum


class GBTBillOfMaterialsExclusionStatus(str, Enum):
    EXCLUDED = "EXCLUDED"
    NOT_EXCLUDED = "NOT_EXCLUDED"
    PARENT_EXCLUDED = "PARENT_EXCLUDED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
