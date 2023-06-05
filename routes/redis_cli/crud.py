from .connection import redis_conn
from redis.exceptions import ResponseError

# CREATE
def save_hash(key: str, data: dict):
    try:
        redis_conn.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)

# READ
def get_hash(key: str):
    try:
        return redis_conn.hgetall(name=key)
    except ResponseError as e:
        print(e)

# DELETE
def delete_hash(key: str, keys: list):
    try:
        redis_conn.hdel(key, *keys)
    except ResponseError as e:
        print(e)