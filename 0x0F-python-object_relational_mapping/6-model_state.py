#!/usr/bin/python3
"""This Module prints all of a database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        """State Class"""
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False,
                    autoincrement=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
    # session = Session(engine)
    # for state in session.query(State).order_by(State.id).all():
    # print("{}: {}".format(state.id, state.name))
    # session.close()
if __name__ == '__main__':
    main()
