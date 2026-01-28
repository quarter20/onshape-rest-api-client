from enum import Enum


class BTWorkflowObserverEntryType(str, Enum):
    ALIAS = "ALIAS"
    ROLE = "ROLE"
    TEAM = "TEAM"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
