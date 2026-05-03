"""
Схемы данных
"""
from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Запрос
    """
    message: str


class ChatResponse(BaseModel):
    """
    Ответ
    """
    response: str
