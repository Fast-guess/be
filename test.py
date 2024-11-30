import aioredis
import asyncio

async def delete_keys():
    redis = await aioredis.from_url("redis://14.225.217.59:6379")
    pattern = "room:*:players"

    # Sử dụng SCAN để tìm key
    async for key in redis.scan_iter(match=pattern):
        await redis.delete(key)
        print(f"Deleted key: {key}")

    await redis.close()

asyncio.run(delete_keys())