#!/usr/bin/python3
"""_summary_
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


if __name__ == "__main__":
    """_summary_
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbs = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, dbs),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)

    session.commit()
    session.close()
