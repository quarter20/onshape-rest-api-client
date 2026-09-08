from enum import StrEnum


class Type(StrEnum):
    APIKEY = "APIKEY"
    HTTP = "HTTP"
    MUTUALTLS = "MUTUALTLS"
    OAUTH2 = "OAUTH2"
    OPENIDCONNECT = "OPENIDCONNECT"

    def __str__(self) -> str:
        return str(self.value)
