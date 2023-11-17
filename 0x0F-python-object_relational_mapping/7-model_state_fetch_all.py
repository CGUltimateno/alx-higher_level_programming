#!/usr/bin/python3
""" Script that lists all State objects from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        for state in session.query(State):
            print(f"{state.id}: {state.name}")
