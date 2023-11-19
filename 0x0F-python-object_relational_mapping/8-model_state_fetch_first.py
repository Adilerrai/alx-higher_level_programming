#!/usr/bin/python3

from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           )

    Session = sessionmaker(bind=engine)
    session = Session()
    if len(sys.argv) == 5:
        filter_name = sys.argv[4]
        states = session.query(State).filter(State.name.like(
            '%{}%'.format(filter_name))).order_by(State.id).all()
    else:
            # If sys.argv[4] is not provided, fetch all states
        states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
