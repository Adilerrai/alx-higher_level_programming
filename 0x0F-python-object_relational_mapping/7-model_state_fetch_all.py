#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    meta = MetaData()
    states = Table('states', meta, autoload_with=engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(states).all()

    for row in result:
        print(row)
