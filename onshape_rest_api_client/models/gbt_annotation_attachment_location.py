from enum import StrEnum


class GBTAnnotationAttachmentLocation(StrEnum):
    BOTTOM_MIDDLE = "BOTTOM_MIDDLE"
    LEFT_MIDDLE = "LEFT_MIDDLE"
    OPPOSITE_LEADER_EDGE = "OPPOSITE_LEADER_EDGE"
    RIGHT_MIDDLE = "RIGHT_MIDDLE"
    TOP_MIDDLE = "TOP_MIDDLE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
