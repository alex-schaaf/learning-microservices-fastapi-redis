from redis_om import get_redis_connection, HashModel
from inventory.config import settings

redis = get_redis_connection(
    host=settings.REDIS_PUBLIC_ENDPOINT,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    decode_responses=True
)