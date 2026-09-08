from enum import StrEnum


class GBTLoadType(StrEnum):
    ACCELERATION = "ACCELERATION"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    BEARING_LOAD = "BEARING_LOAD"
    FORCE = "FORCE"
    MOMENT = "MOMENT"
    PRESSURE = "PRESSURE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
