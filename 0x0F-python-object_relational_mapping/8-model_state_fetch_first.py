#!/usr/bin/python3
"""_summary_
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@\
        localhost:3306/{}'.format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    f_state = session.query(State).order_by(State.id).first()

    if f_state:
        print(f"{f_state.id}: {f_state.name}")
    else:
        print("Nothing")
    session.close()
