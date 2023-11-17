#!/usr/bin/python3
""" Script that adds the State object “Louisiana” to the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql:///{argv[3]}",
                           pool_pre_ping=True)

    Session = sessionmaker(engine)

    with Session() as session:
        state = State()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)