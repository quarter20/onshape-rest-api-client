from enum import StrEnum


class GBTFeatureDimensionType(StrEnum):
    ANGLE = "ANGLE"
    AXIS_DISTANCE = "AXIS_DISTANCE"
    DIAMETER = "DIAMETER"
    DISTANCE = "DISTANCE"
    RADIUS = "RADIUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
