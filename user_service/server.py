from user_pb2_grpc import add_UserAPIServicer_to_server
import grpc
from concurrent import futures
from config import settings
from service import UserAPI
from utils.signal import Signal
import threading


if __name__ == "__main__":
    threading.Thread(target=Signal.listen_heartbeat).start()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=settings.THREAD_MAX_WORKERS))
    add_UserAPIServicer_to_server(UserAPI(), server)
    _url = '{}:{}'.format(settings.GRPC_HOST, settings.GRPC_PORT)
    server.add_insecure_port(_url)
    server.start()
    print(f"gRPC server is running on {_url}")
    server.wait_for_termination()
