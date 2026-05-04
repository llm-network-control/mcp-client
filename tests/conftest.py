"""
Fixtures для тестов
"""
import pytest
from fastapi.testclient import TestClient

from app.server import app


@pytest.fixture
def client() -> TestClient:
    """
    Fixture с тестовым клиентом FastAPI
    """
    return TestClient(app)
