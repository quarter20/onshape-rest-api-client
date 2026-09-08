from enum import StrEnum


class GetRevisionHistoryInCompanyByElementIdWv(StrEnum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
