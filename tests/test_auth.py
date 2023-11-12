import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth0 import authenticate_user, get_user_info, logout_user

client = TestClient(app)

def test_authenticate_user():
    response = authenticate_user("test_username", "test_password")
    assert response.status_code == 200

def test_get_user_info():
    response = get_user_info("test_token")
    assert response.status_code == 200

def test_logout_user():
    response = logout_user("test_token")
    assert response.status_code == 200