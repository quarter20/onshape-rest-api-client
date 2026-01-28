from enum import Enum


class GBTSketchEntityType(str, Enum):
    CIRCLE = "CIRCLE"
    CONIC = "CONIC"
    CURVE = "CURVE"
    CURVED_TEXT = "CURVED_TEXT"
    ELLIPSE = "ELLIPSE"
    IMAGE_ENTITY = "IMAGE_ENTITY"
    LINE = "LINE"
    POINT = "POINT"
    SPLINE = "SPLINE"
    TEXT = "TEXT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
