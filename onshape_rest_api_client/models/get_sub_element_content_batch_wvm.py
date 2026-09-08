from enum import StrEnum


class GetSubElementContentBatchWvm(StrEnum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
