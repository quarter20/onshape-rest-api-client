from enum import StrEnum


class BTWorkflowObserverEntryType(StrEnum):
    ALIAS = "ALIAS"
    ROLE = "ROLE"
    TEAM = "TEAM"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
