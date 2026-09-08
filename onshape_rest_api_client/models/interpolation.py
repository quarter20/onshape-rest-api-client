from enum import StrEnum


class Interpolation(StrEnum):
    CATMULLROMSPLINE = "CATMULLROMSPLINE"
    CUBICSPLINE = "CUBICSPLINE"
    LINEAR = "LINEAR"
    STEP = "STEP"

    def __str__(self) -> str:
        return str(self.value)
