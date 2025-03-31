import redis

# Параметры подключения
REDIS_HOST = "localhost"  # Замените на ваш хост
REDIS_PORT = 6379
REDIS_PASSWORD = ""  # Укажите ваш пароль, если он установлен


def init_redis(
    host: str = REDIS_HOST,
    port: int = REDIS_PORT,
    password: str = REDIS_PASSWORD,
    ssl: bool = True,
) -> redis.Redis:
    """Инициализация подключения к Redis"""
    return redis.Redis(
        host=host,
        port=port,
        password=password,
        ssl=ssl,
        ssl_cert_reqs="none",
    )


def test_redis_connection(client: redis.Redis) -> str:
    """Проверка подключения к Redis"""
    try:
        if client.ping():
            client.set("test_key", "hello_world")
            value = client.get("test_key")
            return f"Подключение успешно! Тест: {value.decode('utf-8')}"
        return "Не удалось подключиться к Redis"
    except Exception as e:
        return f"Ошибка подключения: {e}"


redis_client = init_redis()
print(test_redis_connection(redis_client))