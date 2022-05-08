import os


SERVICE = {
    "type": os.environ.get("SERVICE_TYPE", "service"),
    "name": os.environ.get("SERVICE_NAME", "unnamed"),
}
DATABASE_CONNECTION = "sqlite:///db.sqlite"
GRPC_PORT = int(os.environ.get("SERVICE_GRPC_PORT", "50051"))
GRPC_HOST = os.environ.get("SERVICE_GRPC_HOST", "127.0.0.1")
THREAD_MAX_WORKERS = 10

CONTRACT_HOST = "127.0.0.1"
CONTRACT_PORT = 9001

OTP_OPTIONS = {
    "length": 6,
    "lifespan": 2 * 60,
}

REDIS_OPTIONS = {
    "host": os.environ.get("SERVICE_REDIS_HOST", "127.0.0.1"),
    "port": int(os.environ.get("SERVICE_REDIS_PORT", "6379")),
    "db": os.environ.get("SERVICE_REDIS_DB", "0"),
}
