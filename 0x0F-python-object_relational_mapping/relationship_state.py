#!/usr/bin/python3
''' script that def state'''


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    '''def state'''

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all,delete")
