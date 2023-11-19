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
    pattern = sys.argv[4]
    state = session.query(State).filter(State.name.like(
        '%{}%'.format(pattern))).order_by(State.id).all()

    if state:
        print("{}", format(state.id))
    else:
        print('Not found')
    session.close()
