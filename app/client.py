"""
MCP Клиент
"""
from fastmcp import Client


def get_client(server_host, server_port) -> Client:
    """
    Создание mcp клиента
    """
    client = Client(
        f"http://{server_host}:{server_port}/mcp"
    )
    return client


async def get_tools(mcp_client: Client) -> list[dict]:
    """
    Получаем tools в формате openai
    """
    # 1. Получаем список tools
    async with mcp_client:
        tools = await mcp_client.list_tools()

    # 2. Конвертируем tools в OpenAI-формат
    openai_tools = [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema,
            },
        }
        for tool in tools
    ]
    return openai_tools
