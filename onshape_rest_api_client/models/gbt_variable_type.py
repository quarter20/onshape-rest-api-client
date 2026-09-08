from enum import StrEnum


class GBTVariableType(StrEnum):
    ANGLE = "ANGLE"
    ANY = "ANY"
    LENGTH = "LENGTH"
    NUMBER = "NUMBER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
