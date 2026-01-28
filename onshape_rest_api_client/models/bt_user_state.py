from enum import Enum


class BTUserState(str, Enum):
    ACTIVE = "ACTIVE"
    ALL = "ALL"
    APPROVED = "APPROVED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MARKED_FOR_DELETION = "MARKED_FOR_DELETION"
    REQUESTED = "REQUESTED"
    REQUEST_EXPIRED = "REQUEST_EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
