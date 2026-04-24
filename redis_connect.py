import redis
import time

REDIS_HOST = "host.docker.internal"
REDIS_PORT = 6379
REDIS_PASSWORD = "secret_redis"
REDIS_DB = 0

client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=REDIS_DB,
    decode_responses=True,
)

try:
    client.ping()
    print(f"✅ 已连接 Redis: {REDIS_HOST}:{REDIS_PORT}, db={REDIS_DB}")
except redis.RedisError as exc:
    print(f"❌ Redis 连接失败: {exc}")
    raise

while True:
    try:
        keys = client.keys("*")
        print(f"当前键数量: {len(keys)}")
        for key in keys:
            print(key)
    except redis.RedisError as exc:
        print(f"Redis 读取失败: {exc}")
    time.sleep(5)
