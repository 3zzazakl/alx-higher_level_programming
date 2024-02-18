#!/usr/bin/python3
"""_summary_
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbs = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, passwd, dbs), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    f_state = session.query(State).first()

    if f_state:
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Not found")
    session.close()
