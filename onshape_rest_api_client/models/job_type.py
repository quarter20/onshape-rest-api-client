from enum import Enum


class JobType(str, Enum):
    SYNC_BOM = "SYNC_BOM"
    SYNC_ITEM = "SYNC_ITEM"
    SYNC_RELEASE_CANDIDATE = "SYNC_RELEASE_CANDIDATE"

    def __str__(self) -> str:
        return str(self.value)
