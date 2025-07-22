from fastapi import FastAPI, HTTPException

from models.user_auth import SignupRequest, ConfirmRequest, LoginRequest, RefreshTokenRequest
from services.user_register import RegisterUser as User

app = FastAPI()


@app.post("/signup")
def signup(data: SignupRequest):
    try:
        response = User.sign_up(data.username, data.email, data.password)
        return {"message": "Usuário registrado", "username": response["UserSub"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/confirm")
def confirm(data: ConfirmRequest):
    try:
        User.confirm_sign_up(data.username, data.code)
        return {"message": "Usuário validado com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login")
def do_login(data: LoginRequest):
    try:
        auth_result = User.login(data.username, data.password)
        return auth_result
    except Exception as e:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")


@app.post("/refresh")
def refresh(data: RefreshTokenRequest):
    try:
        tokens = User.refresh_tokens(data.refresh_token)
        return {
            "access_token": tokens["AccessToken"],
            "id_token": tokens["IdToken"],
            "expires_in": tokens["ExpiresIn"],
            "token_type": tokens["TokenType"]
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))