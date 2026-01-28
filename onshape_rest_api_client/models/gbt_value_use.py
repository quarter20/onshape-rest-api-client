from enum import Enum


class GBTValueUse(str, Enum):
    INTEGER = "INTEGER"
    LOCALIZE = "LOCALIZE"
    STRING = "STRING"
    TYPE = "TYPE"
    UNITS = "UNITS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
