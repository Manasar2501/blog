from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

Base = declarative_base()

localSession = sessionmaker(bind=engine, autoflush=False,)