#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=db_engine)
    session = Session()
    for a in session.query(State).order_by(State.id):
        print("{}: {}".format(a.id, a.name))
    for a in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(a.id, a.name, a.state.name))
