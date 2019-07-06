# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey("sources.id"))
    author = Column(String)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    url_to_image = Column(String)
    published_at = Column(Date)
    content = Column(String)
    created_at = Column(Date, default=datetime.utcnow)
    created_by = Column(String, default='nhcli')
    updated_at = Column(Date)
    updated_by = Column(String)

    # articles = relationship("Article", backref="sources", order_by="Source.id")
    source = relationship("Source", backref="articles")

    def __init__(   
        self, author, title, description, url,
        url_to_image, published_at, content, source
    ):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        self.source = source

