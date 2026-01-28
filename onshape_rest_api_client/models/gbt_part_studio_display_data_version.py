from enum import Enum


class GBTPartStudioDisplayDataVersion(str, Enum):
    UNKNOWN = "UNKNOWN"
    V0_ORIGINAL_VERSION = "V0_ORIGINAL_VERSION"
    V1_SMOOTH_EDGES_RENDERING_OPTIONS = "V1_SMOOTH_EDGES_RENDERING_OPTIONS"
    V2_SMOOTH_EDGES_TOLERANCE_CHANGED = "V2_SMOOTH_EDGES_TOLERANCE_CHANGED"

    def __str__(self) -> str:
        return str(self.value)
