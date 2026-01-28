from enum import Enum


class BTESVersionWorkspaceChoice(str, Enum):
    ALL = "ALL"
    VERSIONS = "VERSIONS"
    WORKSPACES = "WORKSPACES"

    def __str__(self) -> str:
        return str(self.value)
