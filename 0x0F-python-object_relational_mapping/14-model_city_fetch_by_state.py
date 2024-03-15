#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=db_engine)
    session = Session()
    for a in (session.query(State.name, City.id, City.name).filter(
              State.id == City.state_id)):
        print("{}: ({:d}) {}".format(a[0], a[1], a[2]))
    session.commit()
    session.close()
