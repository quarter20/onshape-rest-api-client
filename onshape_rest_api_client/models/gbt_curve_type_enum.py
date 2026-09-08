from enum import StrEnum


class GBTCurveTypeEnum(StrEnum):
    BCURVE = "BCURVE"
    CIRCLE = "CIRCLE"
    ELLIPSE = "ELLIPSE"
    ICURVE = "ICURVE"
    LINE = "LINE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
