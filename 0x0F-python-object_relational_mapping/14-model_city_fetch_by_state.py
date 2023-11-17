#!/usr/bin/python3
""" Script that lists all City objects from the database """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        for city in session.query(City):
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))
