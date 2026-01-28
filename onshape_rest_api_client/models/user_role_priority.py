from enum import Enum


class UserRolePriority(str, Enum):
    ADMIN = "ADMIN"
    GUEST = "GUEST"
    MEMBER = "MEMBER"
    OWNER = "OWNER"

    def __str__(self) -> str:
        return str(self.value)
