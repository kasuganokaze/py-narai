import redis

r = redis.Redis(host="127.0.0.1", port=6379, password='123456')
for item in r.lrange("list", 0, -1):
    print(item.decode("utf-8"))
