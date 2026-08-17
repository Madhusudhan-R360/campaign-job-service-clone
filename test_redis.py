# test_redis.py

from db.connection import redis_client

redis_client.set(
    "health",
    "ok"
)

print(
    redis_client.get("health")
)