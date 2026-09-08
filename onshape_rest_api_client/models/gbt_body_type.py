from enum import StrEnum


class GBTBodyType(StrEnum):
    COMPOSITE = "COMPOSITE"
    MATE_CONNECTOR = "MATE_CONNECTOR"
    POINT = "POINT"
    SHEET = "SHEET"
    SOLID = "SOLID"
    UNKNOWN = "UNKNOWN"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
