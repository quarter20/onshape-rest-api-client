from enum import StrEnum


class GetVariableStudioScopeWv(StrEnum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
