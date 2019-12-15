#!/usr/bin/python3
"""This Module prints all of a database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == sys.argv[4])
    a = 0
    for state in query.order_by(State.id).all():
        if state:
            print("{}".format(state.id))
            a = 1
    if a == 0:
        print("Not found")
    session.close()
if __name__ == '__main__':
    main()
