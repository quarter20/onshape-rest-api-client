from enum import Enum


class BTTranslateFormatParamsResolution(str, Enum):
    COARSE = "coarse"
    FINE = "fine"
    MEDIUM = "medium"

    def __str__(self) -> str:
        return str(self.value)
