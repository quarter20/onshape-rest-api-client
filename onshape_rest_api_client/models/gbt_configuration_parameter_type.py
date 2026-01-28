from enum import Enum


class GBTConfigurationParameterType(str, Enum):
    BOOLEAN = "BOOLEAN"
    ENUM = "ENUM"
    QUANTITY = "QUANTITY"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)
