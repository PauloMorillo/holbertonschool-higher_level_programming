#!/usr/bin/python3
"""This Module has a model for create a table in a database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date


Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    # session = Session(engine)
    # for state in session.query(State).order_by(State.id).all():
    # print("{}: {}".format(state.id, state.name))
    # session.close()
