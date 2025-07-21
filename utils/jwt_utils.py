from jose import jwt
import requests
import os

REGION = os.getenv("AWS_REGION")
USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID")
ISSUER = f"https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}"

_jwk_cache = {}

def get_public_keys():
    global _jwk_cache
    if not _jwk_cache:
        jwks_url = f"{ISSUER}/.well-known/jwks.json"
        _jwk_cache = requests.get(jwks_url).json()
    return _jwk_cache['keys']

def decode_token(token):
    keys = get_public_keys()
    headers = jwt.get_unverified_header(token)
    key = next(k for k in keys if k["kid"] == headers["kid"])

    return jwt.decode(
        token,
        key,
        algorithms=["RS256"],
        audience=CLIENT_ID,
        issuer=ISSUER
    )
