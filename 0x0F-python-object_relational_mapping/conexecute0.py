#!/usr/bin/python3
"""This Module prints all of a database"""
import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
conn = engine.connect()
#print(engine.table_names())
meta = MetaData(engine)
#print(meta)
meta.reflect(bind=engine)
#print(meta)
table = meta.tables['states']
select_st = select([table]).order_by(table.c.id)
res = conn.execute(select_st)
for _row in res:
    print(_row)
