from enum import Enum


class BTRole(str, Enum):
    ADMIN = "ADMIN"
    ANONYMOUS = "ANONYMOUS"
    DEVELOPER = "DEVELOPER"
    ONSHAPECOMPANYUSER = "ONSHAPECOMPANYUSER"
    PARTNER = "PARTNER"
    SERVICE = "SERVICE"
    TOTPPENDINGUSER = "TOTPPENDINGUSER"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
