from enum import Enum


class GetWMVEPsMetadataWvm(str, Enum):
    M = "m"
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
