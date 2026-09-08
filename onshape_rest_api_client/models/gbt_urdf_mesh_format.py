from enum import StrEnum


class GBTUrdfMeshFormat(StrEnum):
    GLB = "GLB"
    GLTF = "GLTF"
    OBJ = "OBJ"
    STL = "STL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
