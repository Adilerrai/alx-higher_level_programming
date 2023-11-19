#!/usr/bin/python3
"""This is a script """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for s in states
    print("{}: {}".format(states[s].id, state[s].name))
    session.close()
