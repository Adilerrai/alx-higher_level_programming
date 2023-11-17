#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base

engine = create_engine()


base = declarative_base()


class State(base):
    __tablename__ 