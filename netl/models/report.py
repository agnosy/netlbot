# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    report = Column(String)

    def __init__(self, report):
        self.report = report

