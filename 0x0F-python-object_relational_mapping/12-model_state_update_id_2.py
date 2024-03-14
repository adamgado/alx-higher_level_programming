#!/usr/bin/python3
"""changes the name of a State object"""
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
    updated = session.query(State).filter_by(id=2).first()
    updated.name = 'New Mexico'
    session.commit()
