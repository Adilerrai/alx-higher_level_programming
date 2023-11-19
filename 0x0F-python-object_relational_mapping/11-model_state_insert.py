#!/usr/bin/python3
"""This is a script """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state_name = 'Louisiana'

    # Create a new State instance and add it to the session
    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
