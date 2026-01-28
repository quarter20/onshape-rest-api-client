from enum import Enum


class GBTBodyType(str, Enum):
    COMPOSITE = "COMPOSITE"
    MATE_CONNECTOR = "MATE_CONNECTOR"
    POINT = "POINT"
    SHEET = "SHEET"
    SOLID = "SOLID"
    UNKNOWN = "UNKNOWN"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
