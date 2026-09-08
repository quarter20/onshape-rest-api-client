from enum import StrEnum


class GBTEdgeType(StrEnum):
    CIRCLE = "CIRCLE"
    CONIC = "CONIC"
    ELLIPSE = "ELLIPSE"
    INTERSECTION = "INTERSECTION"
    LINE = "LINE"
    OTHER = "OTHER"
    POLYLINE = "POLYLINE"
    SPCURVE = "SPCURVE"
    SPLINE = "SPLINE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
