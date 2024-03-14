#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
          argv[1], argv[2], argv[3])
    db_engine = create_engine(db)
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)
    session = Session()
    state_obj = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(state_obj[0].id)
    except IndexError:
        print("Not found")
