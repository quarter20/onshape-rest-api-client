from enum import Enum


class BTMetadataValueType(str, Enum):
    BLOB = "BLOB"
    BOOL = "BOOL"
    CATEGORY = "CATEGORY"
    COMPUTED = "COMPUTED"
    DATE = "DATE"
    DOUBLE = "DOUBLE"
    ENUM = "ENUM"
    FOREIGN = "FOREIGN"
    INT = "INT"
    LIST = "LIST"
    OBJECT = "OBJECT"
    STRING = "STRING"
    USER = "USER"
    VALUE_WITH_UNITS = "VALUE_WITH_UNITS"

    def __str__(self) -> str:
        return str(self.value)
