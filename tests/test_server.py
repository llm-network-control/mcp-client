"""
Test app/server
"""
from fastapi.testclient import TestClient

from .mocks import (
    MockAsyncOpenAI,
    MockMCPClient,
    MockMessageWithoutTools,
    MockMessageWithTools,
)

CHAT_URL = '/chat'


def test_chat_without_tools(client: TestClient, mocker):
    """
    Test /chat: positive: with mocks: call without tools
    """
    mocker.patch('app.server.mcp_client', MockMCPClient('test_url'))
    mocker.patch('app.server.llm', MockAsyncOpenAI())
    data = {
        'message': 'Что ты умеешь?'
    }
    response = client.post(CHAT_URL, json=data)
    assert response.status_code == 200
    expected_response = {
        'response': MockMessageWithoutTools().content
    }
    assert response.json() == expected_response


def test_chat_with_tools(client: TestClient, mocker):
    """
    Test /chat: positive: with mocks: call with tools
    """
    mocker.patch('app.server.mcp_client', MockMCPClient())
    mocker.patch('app.server.llm', MockAsyncOpenAI(with_tools=True))
    data = {
        'message': 'Что ты умеешь?'
    }
    response = client.post(CHAT_URL, json=data)
    assert response.status_code == 200
    expected_response = {
        'response': MockMessageWithTools().content
    }
    assert response.json() == expected_response


def test_health_check(client):
    """
    Test /health: positive
    """
    response = client.get('/health')
    assert response.status_code == 200
    expected_response = {
        "status": "healthy",
        "service": "mcp-client"
    }
    assert expected_response == response.json()
