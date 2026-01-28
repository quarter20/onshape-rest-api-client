from enum import Enum


class GetElementThumbnailWithSizeWv(str, Enum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
