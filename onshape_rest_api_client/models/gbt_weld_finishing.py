from enum import Enum


class GBTWeldFinishing(str, Enum):
    CHIPPING = "CHIPPING"
    GRINDING = "GRINDING"
    HAMMERING = "HAMMERING"
    MACHINING = "MACHINING"
    NONE = "NONE"
    ROLLING = "ROLLING"
    UNKNOWN = "UNKNOWN"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
