from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
URI = os.getenv("dburi")

engine = create_engine(URI)
factory = sessionmaker(bind=engine)
base = declarative_base()

def get_new_session():
    session = factory()
    try:
        yield session
    finally:
        session.close()