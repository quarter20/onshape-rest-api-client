from enum import Enum


class GetRevisionHistoryInCompanyByElementIdWv(str, Enum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
