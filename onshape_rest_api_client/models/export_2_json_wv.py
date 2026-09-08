from enum import StrEnum


class Export2JsonWv(StrEnum):
    V = "v"
    W = "w"

    def __str__(self) -> str:
        return str(self.value)
