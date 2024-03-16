#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=db_engine)
    session = Session()
    query = session.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    session.commit()
    session.close()
