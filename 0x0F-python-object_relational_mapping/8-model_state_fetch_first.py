#!/usr/bin/python3
"""Lists the first state"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
