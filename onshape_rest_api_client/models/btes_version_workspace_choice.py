from enum import StrEnum


class BTESVersionWorkspaceChoice(StrEnum):
    ALL = "ALL"
    VERSIONS = "VERSIONS"
    WORKSPACES = "WORKSPACES"

    def __str__(self) -> str:
        return str(self.value)
