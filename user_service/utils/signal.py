from config import settings
import redis
from datetime import datetime
import json


class Signal:
    @staticmethod
    def listen_heartbeat():
        _r = redis.Redis(host=settings.REDIS_OPTIONS["host"], port=settings.REDIS_OPTIONS["port"],
                         db=settings.REDIS_OPTIONS["db"])
        pubsub = _r.pubsub()
        pubsub.subscribe(["heartbeat"])
        while True:
            for item in pubsub.listen():
                Signal.send_ack()

    @staticmethod
    def send_ack():
        _r = redis.Redis(host=settings.REDIS_OPTIONS["host"], port=settings.REDIS_OPTIONS["port"],
                         db=settings.REDIS_OPTIONS["db"])
        _r.publish("heartbeat_ack", json.dumps({
            "service": settings.SERVICE["type"],
            "name": settings.SERVICE["name"],
            "time": datetime.utcnow().timestamp(),
            "host": settings.GRPC_HOST,
            "port": settings.GRPC_PORT,
        }))
