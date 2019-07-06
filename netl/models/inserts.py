# coding=utf-8

# 1 - imports
from datetime import date

from report import Report
from base import Session, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create reports
report1 = Report('{"key1": "value1"}')
report2 = Report('{"key2": "value2"}')
report3 = Report('{"key3": "value3"}')

# 9 - persists data
session.add(report1)
session.add(report2)
session.add(report3)

# 10 - commit and close session
session.commit()
session.close()

