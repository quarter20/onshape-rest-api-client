from enum import Enum


class GBTUrdfMeshFormat(str, Enum):
    GLTF = "GLTF"
    STL = "STL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
