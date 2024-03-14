#!/usr/bin/python3
"""prints all City objects from the database"""
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
    for a in (session.query(State.name, City.id, City.name).filter(
              State.id == City.state_id)):
        print("{}: ({}) {}".format(a[0], str(a[1]), a[2]))
