from enum import Enum


class BTComputedAssemblyPropertyAggregationOperator(str, Enum):
    ALL = "ALL"
    ANY = "ANY"
    AVERAGE = "AVERAGE"
    MAXIMUM = "MAXIMUM"
    MINIMUM = "MINIMUM"
    NOT_ALL = "NOT_ALL"
    NOT_ANY = "NOT_ANY"
    SUM = "SUM"
    WEIGHTED_AVERAGE = "WEIGHTED_AVERAGE"
    WEIGHTED_SUM = "WEIGHTED_SUM"

    def __str__(self) -> str:
        return str(self.value)
