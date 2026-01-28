from enum import Enum


class SetApplicationElementThumbnailWv(str, Enum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
