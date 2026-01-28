from enum import Enum


class BTVersionGraphMode(str, Enum):
    ACTIVE_BRANCH = "ACTIVE_BRANCH"
    ACTIVE_BRANCH_WITH_PARENTS = "ACTIVE_BRANCH_WITH_PARENTS"
    ALL_BRANCHES = "ALL_BRANCHES"
    ALL_BRANCHES_WITH_WORKSPACES = "ALL_BRANCHES_WITH_WORKSPACES"

    def __str__(self) -> str:
        return str(self.value)
