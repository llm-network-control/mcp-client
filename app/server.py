# from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.schemas import ChatResponse, ChatRequest
from app.client import get_client
from app.llm import get_llm, use_llm
from config import SERVER_CONNECTION_HOST, SERVER_PORT
from app.examples import openapi_extra


# @asynccontextmanager
# async def lifespan(current_app: FastAPI):
#     """Lifecycle events для FastAPI."""
#     current_app.state.mcp_client = get_client(SERVER_CONNECTION_HOST, SERVER_PORT)
#     current_app.state.llm = get_llm()
#     await current_app.state.mcp_client.connect()
#     # Startup
#     yield
#     # Shutdown
#     await current_app.state.mcp_client.close()


# app = FastAPI(title='MCP Client REST API', lifespan=lifespan)
app = FastAPI(title='MCP Client REST API')


mcp_client = get_client(SERVER_CONNECTION_HOST, SERVER_PORT)
llm = get_llm()

@app.post("/chat", response_model=ChatResponse, openapi_extra=openapi_extra)
async def chat(request: ChatRequest):
    # mcp_client = app.state.mcp_client
    # llm = app.state.llm
    response_content = await use_llm(llm, request.message, mcp_client)

    return ChatResponse(
        response=response_content
    )
