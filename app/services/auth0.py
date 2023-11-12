import requests
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED
from jose import jwt
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")

def authenticate_user(username: str, password: str) -> Dict:
    url = f"https://{AUTH0_DOMAIN}/oauth/token"
    headers = {"content-type": "application/json"}
    body = {
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "audience": AUTH0_AUDIENCE,
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code != 200:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return response.json()

def get_user_info(token: str) -> Dict:
    url = f"https://{AUTH0_DOMAIN}/userinfo"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Could not retrieve user information",
        )
    return response.json()

def logout_user(token: str) -> Dict:
    url = f"https://{AUTH0_DOMAIN}/v2/logout"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Could not logout user",
        )
    return response.json()