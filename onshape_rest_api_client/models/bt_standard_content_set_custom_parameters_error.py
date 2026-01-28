from enum import Enum


class BTStandardContentSetCustomParametersError(str, Enum):
    FAILED_TO_SPECIFY_REQUIRED_PARAMETER = "FAILED_TO_SPECIFY_REQUIRED_PARAMETER"
    INVALID_PARAMETER_ID = "INVALID_PARAMETER_ID"
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
