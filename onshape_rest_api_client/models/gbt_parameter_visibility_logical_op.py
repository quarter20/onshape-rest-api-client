from enum import Enum


class GBTParameterVisibilityLogicalOp(str, Enum):
    AND = "AND"
    NOT = "NOT"
    OR = "OR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
