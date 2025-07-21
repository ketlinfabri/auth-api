# schemas.py

from pydantic import BaseModel

class AuthRequest(BaseModel):
    email: str
    password: str

class ConfirmRequest(BaseModel):
    email: str
    code: str
