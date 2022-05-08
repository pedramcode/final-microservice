import user_pb2_grpc
import user_pb2
import grpc


if __name__ == "__main__":
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserAPIStub(channel)
        # print(stub.Create(user_pb2.UserCreateRequest(username="pedram", password="123")))
        print(stub.Login(user_pb2.UserLoginRequest(username="pedram", password="123")))
        # print(stub.Issue_otp(user_pb2.IssueOtpRequest(token="ace5f4d8df843e0f4fb4dff3d8e5762c4e26479aaff79273b6b2324ec72ad8d1", type=1)))
        # print(stub.Evaluate_otp(user_pb2.EvaluateOtpRequest(token="ace5f4d8df843e0f4fb4dff3d8e5762c4e26479aaff79273b6b2324ec72ad8d1", otp="416355")))
        # print(stub.Update(user_pb2.UserUpdateRequest(token="ace5f4d8df843e0f4fb4dff3d8e5762c4e26479aaff79273b6b2324ec72ad8d1", firstname="Pedram", lastname="Dehghanpour")))
        # print(stub.Me(user_pb2.UserMeRequest(token="ace5f4d8df843e0f4fb4dff3d8e5762c4e26479aaff79273b6b2324ec72ad8d1")))
        # print(stub.Logout(user_pb2.UserLogoutRequest(token="ace5f4d8df843e0f4fb4dff3d8e5762c4e26479aaff79273b6b2324ec72ad8d1")))
