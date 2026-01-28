from enum import Enum


class GBTEdgeTopology(str, Enum):
    LAMINAR = "LAMINAR"
    ONE_SIDED = "ONE_SIDED"
    TWO_SIDED = "TWO_SIDED"
    UNKNOWN = "UNKNOWN"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
