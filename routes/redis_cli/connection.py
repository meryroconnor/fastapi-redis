import redis

try:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    print("Connected to LOCALHOST REDIS")
except redis.ConnectionError as e:
    print(e)