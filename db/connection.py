import redis
import motor.motor_asyncio

from db.config import settings


mongo_client = (
    motor.motor_asyncio.AsyncIOMotorClient(
        settings.mongo_url
    )
)

db = mongo_client[
    settings.database_name
]


redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    decode_responses=True,
)