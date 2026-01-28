from enum import Enum


class BTMetadataStateType(str, Enum):
    DISCARDED = "DISCARDED"
    IN_PROGRESS = "IN_PROGRESS"
    OBSOLETE = "OBSOLETE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    RELEASED = "RELEASED"

    def __str__(self) -> str:
        return str(self.value)
