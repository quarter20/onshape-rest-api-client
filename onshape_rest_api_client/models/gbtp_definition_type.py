from enum import Enum


class GBTPDefinitionType(str, Enum):
    CONSTANT = "CONSTANT"
    CONST_LAMBDA = "CONST_LAMBDA"
    ENUM = "ENUM"
    FEATURE_DEFINITION = "FEATURE_DEFINITION"
    FILE_HEADER = "FILE_HEADER"
    FUNCTION = "FUNCTION"
    PREDICATE = "PREDICATE"
    UNDOCUMENTABLE = "UNDOCUMENTABLE"
    UNKNOWN = "UNKNOWN"
    USER_TYPE = "USER_TYPE"

    def __str__(self) -> str:
        return str(self.value)
