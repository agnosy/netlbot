# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://ndemo:ndemo@localhost:5432/news')
Session = sessionmaker(bind=engine)

Base = declarative_base()

