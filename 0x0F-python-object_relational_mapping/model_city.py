#!/usr/bin/python3
""" Defines a class that maps to the table cities in the database """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """ Defines a class that maps to the table cities in the database """

    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(ForeignKey("states.id"),
                      nullable=False)
    state = relationship("State", backref="City")
