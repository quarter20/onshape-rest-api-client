from enum import StrEnum


class GetDrawingViewJsonGeometry1Wvm(StrEnum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
