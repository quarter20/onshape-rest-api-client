from enum import Enum


class GetValidRuleOptionsCu(str, Enum):
    C = "c"
    U = "u"

    def __str__(self) -> str:
        return str(self.value)
