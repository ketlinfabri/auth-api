import re
import uuid

import boto3
import os
from dotenv import load_dotenv
from fastapi import Query

load_dotenv()

client = boto3.client("cognito-idp", region_name=os.getenv("AWS_REGION"))
CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID")


def sign_up(username, email, password):
    if re.match(r"[^@]+@[^@]+\.[^@]+", username):
        raise ValueError("Username não pode ter formato de e-mail.")

    return client.sign_up(
        ClientId=CLIENT_ID,
        Username=username,
        Password=password,
        UserAttributes=[
            {"Name": "email", "Value": email}
        ]
    )


def confirm_sign_up(username, code):
    return client.confirm_sign_up(
        ClientId=CLIENT_ID,
        Username=username,
        ConfirmationCode=code
    )


def get_username_by_email(email):
    response = client.list_users(
        UserPoolId=CLIENT_ID,
        Filter=f'email = "{email}"'
    )
    users = response.get("Users", [])
    if not users:
        raise Exception("Usuário não encontrado")
    return users[0]["Username"]


def login(email: str = Query(None), username: str = Query(None), password: str = Query(...)):
    if email:
        username = get_username_by_email(email)
    if not username:
        return {"detail": "Username ou email obrigatório"}

    # agora usa username para login
    try:
        response = client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": username, "PASSWORD": password}
        )
        return response["AuthenticationResult"]
    except client.exceptions.NotAuthorizedException:
        return {"detail": "Credenciais inválidas"}
    except client.exceptions.UserNotConfirmedException:
        return {"detail": "Usuário não confirmado"}
    except Exception as e:
        return {"detail": f"Erro inesperado: {str(e)}"}
