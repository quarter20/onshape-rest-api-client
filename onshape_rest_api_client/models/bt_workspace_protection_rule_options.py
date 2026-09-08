from enum import StrEnum


class BTWorkspaceProtectionRuleOptions(StrEnum):
    FAST_FORWARD_MERGE = "FAST_FORWARD_MERGE"
    MERGE = "MERGE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
