from pydantic import BaseModel


class TokenRequest(BaseModel):
    token: str


# class PushRequest(BaseModel):
#    token: str
