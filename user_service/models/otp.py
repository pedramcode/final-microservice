from config.database import Engine
import enum
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Text, DateTime, Boolean
from sqlalchemy import ForeignKey
from .user import User
from datetime import datetime
from utils.security import generate_otp

engine = Engine()


class OTPType(enum.Enum):
    SMS = 1
    EMAIL = 2


class OTP(engine.model):
    __tablename__ = "otp"

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    code = Column(Text, default=generate_otp, nullable=False)
    type = Column(Enum(OTPType), nullable=False)
    is_used = Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="otps")

    def __repr__(self):
        return "<OTP {}>".format(self.code)
