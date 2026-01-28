from enum import Enum


class GBTSurfaceTypeEnum(str, Enum):
    BLEND = "BLEND"
    BSURFACE = "BSURFACE"
    CONE = "CONE"
    CYLINDER = "CYLINDER"
    OFFSET = "OFFSET"
    OTHER = "OTHER"
    PLANE = "PLANE"
    SPHERE = "SPHERE"
    SPUN = "SPUN"
    SWEEP = "SWEEP"
    TORUS = "TORUS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
