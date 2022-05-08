from hashlib import sha256
from datetime import datetime
import random
from config import settings


def hash_password(password):
    hasher = sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()


def generate_token():
    hasher = sha256()
    text = datetime.now().__str__() + str(random.random() * 10000)
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


def generate_otp():
    code = "".join([random.choice("1234567890") for _ in range(0, settings.OTP_OPTIONS["length"])])
    return code


def authenticate(username, password):
    from config.database import Engine
    from models import User

    engine = Engine()
    _password = hash_password(password)

    with engine.session() as session:
        user = session.query(User).filter_by(username=username, password=_password).first()

    return user
