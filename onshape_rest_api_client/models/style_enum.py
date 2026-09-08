from enum import StrEnum


class StyleEnum(StrEnum):
    DEEP_OBJECT = "DEEP_OBJECT"
    FORM = "FORM"
    PIPE_DELIMITED = "PIPE_DELIMITED"
    SPACE_DELIMITED = "SPACE_DELIMITED"

    def __str__(self) -> str:
        return str(self.value)
