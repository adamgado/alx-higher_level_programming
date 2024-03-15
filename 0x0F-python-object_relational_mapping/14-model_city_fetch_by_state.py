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
    for a, b in session.query(City, State).join(State).all():
        print("{}: ({:d}) {}".format(b.name, a.id, a.name))
    session.commit()
    session.close()
