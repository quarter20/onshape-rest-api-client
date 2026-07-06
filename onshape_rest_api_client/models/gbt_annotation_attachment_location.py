from enum import Enum


class GBTAnnotationAttachmentLocation(str, Enum):
    BOTTOM_MIDDLE = "BOTTOM_MIDDLE"
    OPPOSITE_LEADER_EDGE = "OPPOSITE_LEADER_EDGE"
    TOP_MIDDLE = "TOP_MIDDLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
