from enum import Enum


class GBTLoadType(str, Enum):
    ACCELERATION = "ACCELERATION"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    BEARING_LOAD = "BEARING_LOAD"
    FORCE = "FORCE"
    MOMENT = "MOMENT"
    PRESSURE = "PRESSURE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
