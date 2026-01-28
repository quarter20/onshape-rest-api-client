from enum import Enum


class GetNamedPositionsWvm(str, Enum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
