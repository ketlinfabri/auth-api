from pydantic import BaseModel


class SignupRequest(BaseModel):
    username: str
    email: str
    password: str


class ConfirmRequest(BaseModel):
    username: str
    code: str


class LoginRequest(BaseModel):
    username: str
    password: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str
