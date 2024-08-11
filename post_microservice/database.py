from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

engine = create_engine('postgresql://postgres:1111@localhost:5432/Post')

meta = MetaData()
Base = declarative_base()

Post = Table(
    'posts',
    meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('content', String),
    Column('timestamp', String),
    Column('user_id', Integer)
)


class Posts(Base):
    __table__ = Post


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
