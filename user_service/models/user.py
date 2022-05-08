from config.database import Engine
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, DateTime, Boolean
from datetime import datetime
from utils.security import hash_password
import user_pb2

engine = Engine()


class User(engine.model):
    __tablename__ = "user"

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    firstname = Column(String(64), nullable=True)
    lastname = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    mobile = Column(String(64), nullable=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_mobile_verified = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)

    tokens = relationship("Token", back_populates="user")
    otps = relationship("OTP", back_populates="user")

    def __repr__(self):
        return "<User {}>".format(self.username)

    @staticmethod
    def create_user(username, password):
        with engine.session() as session:
            _user = User(username=username, password=hash_password(password))
            session.add(_user)
            session.commit()
        return _user

    def to_buffer(self):
        _buf = user_pb2.User(
            id=self.id,
            username=self.username,
            created_at=self.created_at.timestamp(),
            updated_at=self.updated_at.timestamp(),
            is_active=self.is_active,
            password="***",
            firstname=self.firstname,
            lastname=self.lastname,
            email=self.email,
            mobile=self.mobile,
            is_superuser=self.is_superuser,
            is_staff=self.is_staff,
            is_mobile_verified=self.is_mobile_verified,
            is_email_verified=self.is_email_verified,
        )
        return _buf

    @staticmethod
    def create_superuser(username, password):
        with engine.session() as session:
            _user = User(username=username, password=hash_password(password), is_superuser=True, is_staff=True)
            session.add(_user)
            session.commit()
        return _user
