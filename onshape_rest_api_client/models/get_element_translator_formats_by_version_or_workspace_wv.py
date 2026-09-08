from enum import StrEnum


class GetElementTranslatorFormatsByVersionOrWorkspaceWv(StrEnum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
