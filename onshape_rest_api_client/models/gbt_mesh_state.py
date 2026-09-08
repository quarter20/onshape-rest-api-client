from enum import StrEnum


class GBTMeshState(StrEnum):
    ALL_MESH = "ALL_MESH"
    MIXED = "MIXED"
    NO_MESH = "NO_MESH"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
