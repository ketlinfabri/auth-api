from fastapi import FastAPI, Depends, HTTPException, status, Header
from register_user.app import sign_up, confirm_sign_up, login
from utils.jwt_utils import decode_token

app = FastAPI()


@app.post("/signup")
def signup(username: str, email: str, password: str):
    try:
        response = sign_up(username, email, password)
        username = response["UserSub"]
        return {f"Usuário registrado. Verifique seu e-mail. Username: {username}"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/confirm")
def confirm(username: str, code: str):
    try:
        confirm_sign_up(username, code)
        return {f"Usuário confirmado."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login")
def do_login(username: str, password: str):
    try:
        auth_result = login(username, password)
        return {
            "id_token": auth_result["IdToken"],
            "access_token": auth_result["AccessToken"]
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")


@app.get("/me")
def me(Authorization: str = Header(...)):
    try:
        token = Authorization.replace("Bearer ", "")
        decoded = decode_token(token)
        return {"user": decoded}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido")
