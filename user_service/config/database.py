from utils import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import DATABASE_CONNECTION
from sqlalchemy.orm import declarative_base


class Engine(metaclass=Singleton):
    def __init__(self):
        self.core = create_engine(DATABASE_CONNECTION)
        self.session = sessionmaker(bind=self.core)
        self.model = declarative_base(name="Model")

    def init_db(self):
        self.model.metadata.create_all(bind=self.core)
