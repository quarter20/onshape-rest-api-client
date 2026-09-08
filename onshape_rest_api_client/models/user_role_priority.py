from enum import StrEnum


class UserRolePriority(StrEnum):
    ADMIN = "ADMIN"
    GUEST = "GUEST"
    MEMBER = "MEMBER"
    OWNER = "OWNER"

    def __str__(self) -> str:
        return str(self.value)
