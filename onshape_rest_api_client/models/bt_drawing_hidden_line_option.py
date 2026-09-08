from enum import StrEnum


class BTDrawingHiddenLineOption(StrEnum):
    DRAFTING = "drafting"
    EXCLUDED = "excluded"
    MARKED = "marked"

    def __str__(self) -> str:
        return str(self.value)
