import re
import boto3

from botocore.exceptions import ClientError
from dotenv import load_dotenv
from config import Config

load_dotenv()

client = boto3.client(Config.get('awsClientCognito'), region_name=Config.get('awsRegion'))
user_pool_id = Config.get("COGNITO_APP_CLIENT_ID")


class RegisterUser:
    @staticmethod
    def sign_up(username, email, password):
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            raise ValueError("Username não pode ter formato de e-mail.")

        return client.sign_up(
            ClientId=user_pool_id,
            Username=username,
            Password=password,
            UserAttributes=[
                {"Name": "email", "Value": email}
            ]
        )

    @staticmethod
    def confirm_sign_up(username, code):
        return client.confirm_sign_up(
            ClientId=user_pool_id,
            Username=username,
            ConfirmationCode=code
        )

    @staticmethod
    def login(username: str, password: str):
        if not username:
            return {"detail": "Username é obrigatório"}

        try:
            response = client.initiate_auth(
                ClientId=user_pool_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password
                }
            )
            return response.get("AuthenticationResult")
        except client.exceptions.NotAuthorizedException:
            return {"detail": "Credenciais inválidas"}
        except client.exceptions.UserNotConfirmedException:
            return {"detail": "Usuário não confirmado"}
        except ClientError as e:
            return {"detail": f"Erro do Cognito: {e.response['Error']['Message']}"}
        except Exception as e:
            import traceback
            return {"detail": str(e), "trace": traceback.format_exc()}

    @staticmethod
    def refresh_tokens(refresh_token: str):
        try:
            response = client.initiate_auth(
                ClientId=user_pool_id,
                AuthFlow="REFRESH_TOKEN_AUTH",
                AuthParameters={
                    "REFRESH_TOKEN": refresh_token
                }
            )
            return response["AuthenticationResult"]
        except ClientError as e:
            raise Exception(e.response["Error"]["Message"])
