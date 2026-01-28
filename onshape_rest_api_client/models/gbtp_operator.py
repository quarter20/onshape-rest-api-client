from enum import Enum


class GBTPOperator(str, Enum):
    AND = "AND"
    CONCATENATE = "CONCATENATE"
    CONDITIONAL = "CONDITIONAL"
    DIVIDE = "DIVIDE"
    EQUAL_TO = "EQUAL_TO"
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    MINUS = "MINUS"
    MODULUS = "MODULUS"
    NEGATE = "NEGATE"
    NONE = "NONE"
    NOT = "NOT"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    OR = "OR"
    PLUS = "PLUS"
    POWER = "POWER"
    TIMES = "TIMES"
    UNDEFINED_COALESCING = "UNDEFINED_COALESCING"

    def __str__(self) -> str:
        return str(self.value)
