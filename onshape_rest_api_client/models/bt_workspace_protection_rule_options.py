from enum import Enum


class BTWorkspaceProtectionRuleOptions(str, Enum):
    FAST_FORWARD_MERGE = "FAST_FORWARD_MERGE"
    MERGE = "MERGE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
