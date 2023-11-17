#!/usr/bin/python3
""" Script that lists all State objects that contain the letter a from the
database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        for state in session.query(State).filter(State.name.like('%a%')):
            print(f"{state.id}: {state.name}")
