from enum import Enum


class Type(str, Enum):
    APIKEY = "APIKEY"
    HTTP = "HTTP"
    MUTUALTLS = "MUTUALTLS"
    OAUTH2 = "OAUTH2"
    OPENIDCONNECT = "OPENIDCONNECT"

    def __str__(self) -> str:
        return str(self.value)
