"""
REST API Server
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.client import get_client
from app.examples import openapi_extra
from app.llm import get_llm, use_llm
from app.schemas import ChatRequest, ChatResponse
from config import SERVER_CONNECTION_HOST, SERVER_PORT

app = FastAPI(title='MCP Client REST API')


mcp_client = get_client(SERVER_CONNECTION_HOST, SERVER_PORT)
llm = get_llm()


@app.post("/chat", response_model=ChatResponse, openapi_extra=openapi_extra)
async def chat(request: ChatRequest):
    """
    Обработка запроса пользователя
    """
    response_content = await use_llm(llm, request.message, mcp_client)

    return ChatResponse(
        response=response_content
    )


@app.get("/health")
async def health_check():
    """
    Health Check
    """
    return JSONResponse({
        "status": "healthy",
        "service": "mcp-client"
    })
