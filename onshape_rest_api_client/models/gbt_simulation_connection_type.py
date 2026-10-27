from enum import StrEnum


class GBTSimulationConnectionType(StrEnum):
    BALL = "BALL"
    CUSTOM_BOUNDARY_CONDITION = "CUSTOM_BOUNDARY_CONDITION"
    CYLINDRICAL = "CYLINDRICAL"
    FASTENED = "FASTENED"
    GROUP = "GROUP"
    MULTIPLE = "MULTIPLE"
    PLANAR = "PLANAR"
    REVOLUTE = "REVOLUTE"
    SIMULATION_BONDED = "SIMULATION_BONDED"
    SLIDER = "SLIDER"
    UNCONSTRAINED = "UNCONSTRAINED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
