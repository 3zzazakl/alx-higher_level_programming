#!/usr/bin/python3
"""_summary_
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """_summary_
    """
    engine = create_engine('mysql+mysqldb://{}:{}@\
        localhost:3306/{}'.format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    f_state = session.query(State).filter(State.name == sys.argv[4]).first()
    if f_state:
        print(f"{f_state.id}")
    else:
        print("Not found")
    session.close()
