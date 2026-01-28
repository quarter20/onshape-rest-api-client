from enum import Enum


class ElementType(str, Enum):
    MAT2 = "MAT2"
    MAT3 = "MAT3"
    MAT4 = "MAT4"
    SCALAR = "SCALAR"
    VEC2 = "VEC2"
    VEC3 = "VEC3"
    VEC4 = "VEC4"

    def __str__(self) -> str:
        return str(self.value)
