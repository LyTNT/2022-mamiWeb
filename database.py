#pip install psycopg2-binary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
"""code for heroku deployment"""
import os

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')
if SQLALCHEMY_DATABASE_URL.startswith('postgres://'):
    SQLALCHEMY_DATABASE_URL= SQLALCHEMY_DATABASE_URL.replace('postgres://','postgresql://',1)
"""SAMPLE SYNTAX
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/TodoAppDB"
"""
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
