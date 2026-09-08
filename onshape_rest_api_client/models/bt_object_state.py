from enum import StrEnum


class BTObjectState(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    TRASH = "TRASH"

    def __str__(self) -> str:
        return str(self.value)
