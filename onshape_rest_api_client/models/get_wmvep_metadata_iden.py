from enum import StrEnum


class GetWmvepMetadataIden(StrEnum):
    P = "p"
    PI = "pi"

    def __str__(self) -> str:
        return str(self.value)
