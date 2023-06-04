from connection import r
from redis.exceptions import ResponseError

# CREATE
def save_hash(key: str, data: dict):
    try:
        r.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)

# READ
def get_hash(key: str):
    try:
        return r.hgetall(name=key)
    except ResponseError as e:
        print(e)

# DELETE
def delete_hash(key: str, keys: list):
    try:
        r.hdel(key, *keys)
    except ResponseError as e:
        print(e)