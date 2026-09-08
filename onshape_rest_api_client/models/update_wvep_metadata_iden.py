from enum import StrEnum


class UpdateWvepMetadataIden(StrEnum):
    P = "p"
    PI = "pi"

    def __str__(self) -> str:
        return str(self.value)
