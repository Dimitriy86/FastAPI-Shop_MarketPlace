from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

engine = create_engine(
    setting.database_url,
    connect_arhs={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autopush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
    