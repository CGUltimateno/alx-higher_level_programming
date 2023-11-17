#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument from
the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)
    Session = sessionmaker(engine)

    with Session() as session:
        state = session.query(State).filter(
            State.name == argv[4])
        if state.count() == 0:
            print("Not found")
        else:
            for state in states:
                print(f"{state.id}")