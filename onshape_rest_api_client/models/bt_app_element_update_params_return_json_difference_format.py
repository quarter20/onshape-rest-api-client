from enum import StrEnum


class BTAppElementUpdateParamsReturnJsonDifferenceFormat(StrEnum):
    DEFAULT = "default"
    FULL_PATH = "full_path"
    JSON_PATCH = "json_patch"

    def __str__(self) -> str:
        return str(self.value)
