from enum import Enum


class GBTGraphicsPrimitiveType(str, Enum):
    INFINITE_LINES = "INFINITE_LINES"
    LINES = "LINES"
    POINTS = "POINTS"
    PRIMITIVE_LINE = "PRIMITIVE_LINE"
    SILHOUETTES = "SILHOUETTES"
    TRIANGLES = "TRIANGLES"
    TRIANGLE_STRIP = "TRIANGLE_STRIP"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
