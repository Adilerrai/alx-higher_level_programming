#!/usr/bin/python3

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
    states = session.query(State).order_by(State.id).first()
    if states:
        print("{}: {}".format(state[0].id, state[0].name))
    else:
        print('Nothing')
    session.close()
