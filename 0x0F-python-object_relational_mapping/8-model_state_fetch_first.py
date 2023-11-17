#!/usr/bin/python3
""" Script that lists the first State from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        first_state = session.query(State).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
