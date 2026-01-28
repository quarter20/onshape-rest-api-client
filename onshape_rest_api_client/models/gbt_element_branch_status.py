from enum import Enum


class GBTElementBranchStatus(str, Enum):
    CREATED = "CREATED"
    DELETED = "DELETED"
    EDITS = "EDITS"
    NOT_ON_THIS_BRANCH = "NOT_ON_THIS_BRANCH"
    NO_CHANGES = "NO_CHANGES"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
