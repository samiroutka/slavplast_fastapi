from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# database_url = 'sqlite:///./database.sqlite3'
# -----------------
DATABASE = 'slavplast'
USER = 'admin'
PASSWORD = 'admin'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'postgres'
database_url = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME }'

# engine = create_engine(database_url, connect_args={'check_same_thread': False})
engine = create_engine(database_url)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()

def get_session():
  db_session = SessionLocal()
  try:
    yield db_session
  finally:
    db_session.close()

