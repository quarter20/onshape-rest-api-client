from enum import StrEnum


class BTOwnerType(StrEnum):
    COMPANY = "COMPANY"
    ONSHAPE = "ONSHAPE"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
