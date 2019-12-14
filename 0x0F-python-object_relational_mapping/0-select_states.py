#!/usr/bin/python3
"""This Module prints all of a database"""
import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        """Class state"""
        __tablename__ = 'states'
        id = Column(Integer)
        name = Column(String(256), primary_key=True)

        def __init__(self, name):
            """All begins here"""
            self.name = name

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("({}, '{}')".format(state.id, state.name))
    session.close()
if __name__ == "__main__":
    main()
