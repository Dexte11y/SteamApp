from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

sqlalchemy_database_url = "sqlite:///sql_app.db"
engine = create_engine(
    sqlalchemy_database_url
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
