from enum import Enum


class Interpolation(str, Enum):
    CATMULLROMSPLINE = "CATMULLROMSPLINE"
    CUBICSPLINE = "CUBICSPLINE"
    LINEAR = "LINEAR"
    STEP = "STEP"

    def __str__(self) -> str:
        return str(self.value)
