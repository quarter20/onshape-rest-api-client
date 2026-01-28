from enum import Enum


class GBTMeshState(str, Enum):
    ALL_MESH = "ALL_MESH"
    MIXED = "MIXED"
    NO_MESH = "NO_MESH"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
