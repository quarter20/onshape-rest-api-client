from enum import Enum


class GBTEntityType(str, Enum):
    BODY = "BODY"
    DEGENERATE_EDGE = "DEGENERATE_EDGE"
    EDGE = "EDGE"
    FACE = "FACE"
    UNKNOWN = "UNKNOWN"
    VERTEX = "VERTEX"

    def __str__(self) -> str:
        return str(self.value)
