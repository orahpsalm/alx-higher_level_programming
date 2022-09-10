#!/usr/bin/python3
"""List id of the state passed in argument"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    state = session.query(State).filter(State.name.like(sys.argv[4])).first()
    if state is None:
        print('Not found')
    else:
        print("{}".format(state.id))
    session.close()
