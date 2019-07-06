# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base
from .base import Session


class Source(Base):
    __tablename__ = 'sources'

    id = Column(Integer, primary_key=True)
    text_id = Column(String)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    category = Column(String)
    language = Column(String)
    country = Column(String)
    created_at = Column(Date, default=datetime.utcnow())
    created_by = Column(String, default='netlbot')
    updated_at = Column(Date)
    updated_by = Column(String)

    def __init__(   
        self, text_id, name, description, url,
        category, language, country
    ):
        self.text_id = text_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

