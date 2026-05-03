import json
from fastmcp import Client
from openai import AsyncOpenAI
from .client import get_tools
from config import OPENROUTER_API_KEY

# SYSTEM_PROMPT = '''
# You are a network assistant.
# Use tools to answer questions about routers and networks.
# '''

SYSTEM_PROMPT = '''
You are a network assistant.
Use tools to answer questions about routers and networks.

Rules:
- Only use data returned by tools
- Do not invent or assume additional devices
- If the list is complete, say it explicitly
- Do not say "and others" unless tool explicitly returned truncated data
- Be precise and factual

When listing routers:
- Show all routers returned by the tool
- Use a numbered list
- Do not omit items
- Do not add extra commentary like "and others
'''


def get_llm() -> AsyncOpenAI:
    """
    Получить класс LLM
    """
    return AsyncOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        timeout=20.0,
    )


async def use_llm(
        llm: AsyncOpenAI,
        request: str,
        mcp_client: Client
    ) -> str:
    """
    Использовать llm для обработки запроса
    """
    tools = await get_tools(mcp_client)
    response = await llm.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a network assistant. "
                    "Use tools to answer questions about routers and networks."
                ),
            },
            {
                "role": "user",
                "content": request,
            },
        ],
        tools=tools,
    )

    message = response.choices[0].message

    # Если LLM хочет вызвать tool
    if message.tool_calls:
        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        args = json.loads(arguments)

        # 5. Вызываем MCP tool
        async with mcp_client:
            tool_result = await mcp_client.call_tool(
                tool_name,
                args
            )

        # Второй вызов LLM (с результатом tool)
        final_response = await llm.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a network assistant.",
                },
                {
                    "role": "user",
                    "content": request,
                },
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result),
                },
            ],
        )

        return final_response.choices[0].message.content

    # Если tool не нужен
    return message.content
