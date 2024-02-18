#!/usr/bin/python3
"""_summary_
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """_summary_
    """
    engine = create_engine('mysql+mysqldb://{}:{}@\
        localhost/{}'.format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print("{:d}".format(new_state.id))
    session.close()
