from config.database import Engine
from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .user import User
from datetime import datetime
from utils.security import generate_token

engine = Engine()


class Token(engine.model):
    __tablename__ = "token"

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    code = Column(Text, default=generate_token, nullable=False)

    user = relationship("User", back_populates="tokens")

    def __repr__(self):
        return "<Token {}>".format(self.code)
