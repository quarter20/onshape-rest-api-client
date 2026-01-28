from enum import Enum


class BTRestUserRole(str, Enum):
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
