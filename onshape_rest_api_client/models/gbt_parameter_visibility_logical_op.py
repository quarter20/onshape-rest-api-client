from enum import StrEnum


class GBTParameterVisibilityLogicalOp(StrEnum):
    AND = "AND"
    NOT = "NOT"
    OR = "OR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
