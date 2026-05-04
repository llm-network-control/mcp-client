"""
Моки для тестов
"""
import json


class MockMCPClient:
    """
    Mock: from fastmcp import Client
    """

    def __init__(self, *_, **__):
        pass

    async def __aenter__(self):
        """
        for with enter
        """

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        for with exit
        """

    async def list_tools(self):
        """
        list_tools
        """
        return []

    async def call_tool(self, *args, **kwargs):
        """
        call_tool
        """


class MockFunction:
    """
    Mock: tool_call.function
    """

    def __init__(self):
        self.name = 'test_name'
        self.arguments = json.dumps({})


class MockToolCall:
    """
    Mock: tool_call = message.tool_calls[0]
    """

    def __init__(self):
        self.id = 0
        self.function = MockFunction()


class MockMessageWithTools:
    """
    Mock: message = response.choices[0].message: with tools
    """

    def __init__(self):
        self.tool_calls = [MockToolCall()]
        self.content = 'Я вызвал tool'


class MockMessageWithoutTools:
    """
    Mock: message = response.choices[0].message: without tools
    """

    def __init__(self):
        self.tool_calls = False
        self.content = 'Я у правляю роутерами'


class MockMessage:
    """
    Mock: message = response.choices[0]
    """

    def __init__(self, with_tools):
        self.message = MockMessageWithTools() \
            if with_tools else MockMessageWithoutTools()


class MockResponse:
    """
    Mock response = llm.chat.completions.create(...)
    """

    def __init__(self, with_tools):
        self.choices = [MockMessage(with_tools=with_tools)]


class MockCompletions:
    """
    Mock: llm.chat.completions
    """

    def __init__(self, with_tools):
        self.with_tools = with_tools

    async def create(self, *_, **__):
        """
        llm.chat.completions.create
        """
        return MockResponse(with_tools=self.with_tools)


class MockChat:
    """
    Mock: llm.chat
    """

    def __init__(self, with_tools):
        self.completions = MockCompletions(with_tools=with_tools)


class MockAsyncOpenAI:
    """
    Mock: from openai import AsyncOpenAI
    """

    def __init__(self, with_tools=False):
        self.chat = MockChat(with_tools=with_tools)
