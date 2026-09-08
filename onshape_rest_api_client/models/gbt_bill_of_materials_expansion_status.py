from enum import StrEnum


class GBTBillOfMaterialsExpansionStatus(StrEnum):
    COLLAPSED = "COLLAPSED"
    EXPANDED = "EXPANDED"
    NOT_EXPANDABLE = "NOT_EXPANDABLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
