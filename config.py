from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base

Base: DeclarativeMeta = declarative_base()

DB_ENGINE = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres")
