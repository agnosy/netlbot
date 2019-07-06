# coding=utf-8

# 1 - imports
from report import Report
from base import Session
from datetime import date

# 2 - extract a session
session = Session()

# 3 - extract all reports
reports = session.query(Report).all()

# 4 - print movies' details
print('\n### All reports:')
for report in reports:
    print(f'report: {report.report}')
print('')

