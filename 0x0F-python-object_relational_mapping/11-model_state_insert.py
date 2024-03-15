#!/usr/bin/python3
"""adds the State object Louisiana to database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=db_engine)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    new_obj = session.query(State).filter_by(name='Louisiana').first()
    print(new_obj.id)
    session.commit()
