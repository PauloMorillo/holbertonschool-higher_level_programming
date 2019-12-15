#!/usr/bin/python3
"""This Module prints all of a database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)


    session = Session()
    a = 0
    for state in session.query(State).order_by(State.id).all():
        if state:
            if a == 0:
                print("{}: {}".format(state.id, state.name))
                break
        else:
            print("Nothing")
        a = a + 1
    session.close()
if __name__ == '__main__':
    main()
