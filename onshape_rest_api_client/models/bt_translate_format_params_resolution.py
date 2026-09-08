from enum import StrEnum


class BTTranslateFormatParamsResolution(StrEnum):
    COARSE = "coarse"
    FINE = "fine"
    MEDIUM = "medium"

    def __str__(self) -> str:
        return str(self.value)
