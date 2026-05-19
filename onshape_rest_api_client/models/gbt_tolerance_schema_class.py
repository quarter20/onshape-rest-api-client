from enum import Enum


class GBTToleranceSchemaClass(str, Enum):
    CHAMFER_ANGLE = "CHAMFER_ANGLE"
    CHAMFER_DISTANCE = "CHAMFER_DISTANCE"
    FILLET_RADIUS = "FILLET_RADIUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
