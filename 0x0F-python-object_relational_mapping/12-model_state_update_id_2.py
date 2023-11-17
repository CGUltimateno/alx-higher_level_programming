#!/usr/bin/python3
""" Script that changes the name of a State object from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        state = session.query(State).get(2)
        state.name = "New Mexico"
        state.add(state)
        session.commit()
