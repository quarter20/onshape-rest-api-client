from enum import StrEnum


class BTRestUserRole(StrEnum):
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
