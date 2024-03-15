#!/usr/bin/python3
"""changes the name of a State object"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=db_engine)
    session = Session()
    updated = session.query(State).filter_by(id=2).first()
    updated.name = 'New Mexico'
    session.commit()
