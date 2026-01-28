from enum import Enum


class BTObjectState(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    TRASH = "TRASH"

    def __str__(self) -> str:
        return str(self.value)
