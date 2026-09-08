from enum import StrEnum


class GBTSketchCurveType(StrEnum):
    BEZIER_CURVE = "BEZIER_CURVE"
    INTERPOLATED_SPLINE = "INTERPOLATED_SPLINE"
    UNKNOWN = "UNKNOWN"
    UNSET = "UNSET"

    def __str__(self) -> str:
        return str(self.value)
