import user_pb2
from config.database import Engine
from user_pb2_grpc import UserAPIServicer
import grpc
from config import settings
from models import User, Token, OTP, OTPType
from utils.security import hash_password
from datetime import datetime, timedelta


engine = Engine()
engine.init_db()


class UserAPI(UserAPIServicer):
    def Create(self, request, context):
        with engine.session() as session:
            exists = session.query(User).filter_by(username=request.username)
            if exists.count() != 0:
                return context.abort(grpc.StatusCode.ALREADY_EXISTS, "Username already exists")
            user = User(
                username=request.username,
                password=hash_password(request.password),
                email=request.email,
                mobile=request.mobile,
            )
            session.add(user)
            session.commit()
            return user.to_buffer()

    def Me(self, request, context):
        with engine.session() as session:
            token = session.query(Token).filter_by(code=request.token).first()
            if not token:
                return context.abort(grpc.StatusCode.UNAUTHENTICATED, "Unauthenticated request")
            return token.user.to_buffer()

    def Update(self, request, context):
        with engine.session() as session:
            token = session.query(Token).filter_by(code=request.token).first()
            if not token:
                return context.abort(grpc.StatusCode.UNAUTHENTICATED, "Unauthenticated request")

            token.user.firstname = request.firstname
            token.user.lastname = request.lastname
            session.commit()

            return token.user.to_buffer()

    def Login(self, request, context):
        with engine.session() as session:
            user = session.query(User).filter_by(username=request.username, password=hash_password(request.password))\
                .first()
            if not user:
                return context.abort(grpc.StatusCode.ABORTED, "Username or password is wrong")
            token = session.query(Token).filter_by(user_id=user.id).first()
            if not token:
                token = Token(
                    user_id=user.id,
                )
                session.add(token)
                session.commit()
            return user_pb2.UserLoginResponse(token=token.code)

    def Logout(self, request, context):
        with engine.session() as session:
            token = session.query(Token).filter_by(code=request.token)
            if not token.first():
                return context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")
            token.delete()
            session.commit()
            return user_pb2.MessageResponse(success=True, msg="User logout successfully")

    def Issue_otp(self, request, context):
        with engine.session() as session:
            token = session.query(Token).filter_by(code=request.token).first()
            if not token:
                return context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")
            user = token.user
            otp_type = OTPType(request.type)
            otp = OTP(user_id=user.id, type=otp_type)
            session.add(otp)
            session.commit()
            print("OTP: " + str(otp.code))

            # Send OTP to mobile or email here...

            return user_pb2.MessageResponse(success=True, msg="OTP has been send")

    def Evaluate_otp(self, request, context):
        with engine.session() as session:
            token = session.query(Token).filter_by(code=request.token).first()
            if not token:
                return context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")
            otp = session.query(OTP).filter_by(code=request.otp, user_id=token.user.id, is_used=False).first()
            if not otp:
                return context.abort(grpc.StatusCode.ABORTED, "OTP is invalid")
            if otp.created_at + timedelta(seconds=settings.OTP_OPTIONS["lifespan"]) < datetime.utcnow():
                return context.abort(grpc.StatusCode.ABORTED, "OTP is invalid")
            otp.is_used = True
            session.commit()
            return user_pb2.MessageResponse(success=True, msg="OTP is valid")
