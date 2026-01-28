from enum import Enum


class GBTBillOfMaterialsExpansionStatus(str, Enum):
    COLLAPSED = "COLLAPSED"
    EXPANDED = "EXPANDED"
    NOT_EXPANDABLE = "NOT_EXPANDABLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
