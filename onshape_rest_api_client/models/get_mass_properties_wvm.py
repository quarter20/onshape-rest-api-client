from enum import StrEnum


class GetMassPropertiesWvm(StrEnum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
