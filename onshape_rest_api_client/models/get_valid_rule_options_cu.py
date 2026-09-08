from enum import StrEnum


class GetValidRuleOptionsCu(StrEnum):
    C = "c"
    U = "u"

    def __str__(self) -> str:
        return str(self.value)
