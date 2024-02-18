#!/usr/bin/python3
"""_summary_
"""

import sys
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City, Base

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

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.commit()
    session.close()
