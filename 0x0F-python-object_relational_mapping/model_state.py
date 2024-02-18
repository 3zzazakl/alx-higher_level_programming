#!/usr/bin/python3
"""_summary_
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
