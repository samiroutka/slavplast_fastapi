from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = 'sqlite:///./database.sqlite3'
engine = create_engine(database_url, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()

def get_session():
  db_session = SessionLocal()
  try:
    yield db_session
  finally:
    db_session.close()

