from enum import Enum


class GBTPType(str, Enum):
    ARRAY = "ARRAY"
    BOOLEAN = "BOOLEAN"
    BOX = "BOX"
    BUILTIN = "BUILTIN"
    FUNCTION = "FUNCTION"
    MAP = "MAP"
    NUMBER = "NUMBER"
    STRING = "STRING"
    UNDEFINED = "UNDEFINED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
