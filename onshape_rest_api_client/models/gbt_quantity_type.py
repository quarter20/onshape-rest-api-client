from enum import Enum


class GBTQuantityType(str, Enum):
    ACCELERATION = "ACCELERATION"
    ANGLE = "ANGLE"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    ANYTHING = "ANYTHING"
    ANYTHING_WITH_UNITS = "ANYTHING_WITH_UNITS"
    AREA = "AREA"
    BOOLEAN = "BOOLEAN"
    CURRENT = "CURRENT"
    DENSITY = "DENSITY"
    ENERGY = "ENERGY"
    FORCE = "FORCE"
    INTEGER = "INTEGER"
    LENGTH = "LENGTH"
    MASS = "MASS"
    MOMENT = "MOMENT"
    PRESSURE = "PRESSURE"
    REAL = "REAL"
    STRING = "STRING"
    TEMPERATURE = "TEMPERATURE"
    TIME = "TIME"
    UNKNOWN = "UNKNOWN"
    VOLUME = "VOLUME"

    def __str__(self) -> str:
        return str(self.value)
