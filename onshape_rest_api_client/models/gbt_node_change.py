from enum import Enum


class GBTNodeChange(str, Enum):
    ADDED = "ADDED"
    DELETED = "DELETED"
    MODIFIED = "MODIFIED"
    MOVED = "MOVED"
    MOVED_AND_MODIFIED = "MOVED_AND_MODIFIED"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
