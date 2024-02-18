#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)

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
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, dbs), pool_pre_ping=True)
    Base.metadata.create_all(engine)
