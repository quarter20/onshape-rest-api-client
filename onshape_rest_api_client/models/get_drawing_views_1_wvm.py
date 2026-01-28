from enum import Enum


class GetDrawingViews1Wvm(str, Enum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
