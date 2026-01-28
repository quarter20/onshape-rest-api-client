from enum import Enum


class GBTSurfaceType(str, Enum):
    CONE = "CONE"
    CYLINDER = "CYLINDER"
    EXTRUDED = "EXTRUDED"
    MESH = "MESH"
    OTHER = "OTHER"
    PLANE = "PLANE"
    REVOLVED = "REVOLVED"
    SPHERE = "SPHERE"
    SPLINE = "SPLINE"
    TORUS = "TORUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
