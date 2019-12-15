#!/usr/bin/python3
"""This Module add a state to table states of a database"""
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
    stat = State(name="Louisiana")
    state = [stat]
    session.add_all(state)
    session.commit()
    print(stat.id)
    session.close()
if __name__ == '__main__':
    main()
