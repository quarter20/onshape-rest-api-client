from enum import Enum


class BTDrawingHiddenLineOption(str, Enum):
    DRAFTING = "drafting"
    EXCLUDED = "excluded"
    MARKED = "marked"

    def __str__(self) -> str:
        return str(self.value)
