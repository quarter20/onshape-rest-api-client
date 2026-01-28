from enum import Enum


class GBTVariableType(str, Enum):
    ANGLE = "ANGLE"
    ANY = "ANY"
    LENGTH = "LENGTH"
    NUMBER = "NUMBER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
