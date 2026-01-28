from enum import Enum


class GBTUrdfMeshFormat(str, Enum):
    GLTF = "GLTF"
    STEP = "STEP"
    STL = "STL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
