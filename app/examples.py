examples = {
    "list_routers": {
        "summary": "Список всех роутеров",
        "value": {
            "message": "Покажи все доступные роутеры"
        },
    },
    "get_router": {
        "summary": "Поиск по IP",
        "value": {
            "message": "Найди роутер с IP 192.168.1.1"
        },
    },
    "find_by_ssid": {
        "summary": "Поиск по SSID",
        "value": {
            "message": "Найди роутеры с WiFi сетью MyHomeWiFi"
        },
    },
}



openapi_extra={
    "requestBody": {
        "content": {
            "application/json": {
                "examples": examples
            }
        }
    }
}
