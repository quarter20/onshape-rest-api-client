from enum import Enum


class GBTCurveTypeEnum(str, Enum):
    BCURVE = "BCURVE"
    CIRCLE = "CIRCLE"
    ELLIPSE = "ELLIPSE"
    ICURVE = "ICURVE"
    LINE = "LINE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
