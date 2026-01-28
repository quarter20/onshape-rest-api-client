from enum import Enum


class GBTGeometryType(str, Enum):
    ALL_MESH = "ALL_MESH"
    ARC = "ARC"
    CIRCLE = "CIRCLE"
    CONE = "CONE"
    CONIC = "CONIC"
    CYLINDER = "CYLINDER"
    ELLIPSE = "ELLIPSE"
    ELLIPTICAL_ARC = "ELLIPTICAL_ARC"
    EXTRUDED = "EXTRUDED"
    LINE = "LINE"
    MESH = "MESH"
    MIXED_MESH = "MIXED_MESH"
    PLANE = "PLANE"
    REVOLVED = "REVOLVED"
    SPHERE = "SPHERE"
    SPLINE = "SPLINE"
    SPLINE_CONTROL_POLYGON = "SPLINE_CONTROL_POLYGON"
    SPLINE_INTERNAL_POINT = "SPLINE_INTERNAL_POINT"
    TORUS = "TORUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
