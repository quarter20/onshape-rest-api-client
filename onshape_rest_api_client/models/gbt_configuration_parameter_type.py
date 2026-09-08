from enum import StrEnum


class GBTConfigurationParameterType(StrEnum):
    BOOLEAN = "BOOLEAN"
    ENUM = "ENUM"
    QUANTITY = "QUANTITY"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)
