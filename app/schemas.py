from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    # message: str = Field(
    #     ...,
    #     description="User message to LLM agent",
    #     json_schema_extra={
    #         "examples": [
    #             {
    #                 "message": "Покажи все доступные роутеры"
    #             },
    #             {
    #                 "message": "Найди роутер с IP 192.168.1.1"
    #             },
    #             {
    #                 "message": "Найди роутеры с WiFi сетью MyHomeWiFi"
    #             },
    #         ]
    #     }
    # )


class ChatResponse(BaseModel):
    response: str