from enum import Enum


class GBTFeatureDimensionType(str, Enum):
    ANGLE = "ANGLE"
    AXIS_DISTANCE = "AXIS_DISTANCE"
    DIAMETER = "DIAMETER"
    DISTANCE = "DISTANCE"
    RADIUS = "RADIUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
