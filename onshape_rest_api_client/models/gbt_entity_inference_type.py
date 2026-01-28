from enum import Enum


class GBTEntityInferenceType(str, Enum):
    BOTTOM_AXIS_POINT = "BOTTOM_AXIS_POINT"
    CENTER = "CENTER"
    CENTROID = "CENTROID"
    LOOP_CENTER = "LOOP_CENTER"
    MID_AXIS_POINT = "MID_AXIS_POINT"
    MID_POINT = "MID_POINT"
    ORIGIN_X = "ORIGIN_X"
    ORIGIN_Y = "ORIGIN_Y"
    ORIGIN_Z = "ORIGIN_Z"
    PART_ORIGIN = "PART_ORIGIN"
    POINT = "POINT"
    TOP_AXIS_POINT = "TOP_AXIS_POINT"
    UNKNOWN = "UNKNOWN"
    VIRTUAL_SHARP = "VIRTUAL_SHARP"

    def __str__(self) -> str:
        return str(self.value)
