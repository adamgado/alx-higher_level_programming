#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)
    Session = sessionmaker(bind=db_engine)
    session = Session()
    new_s = State(name='California')
    new_c = City(name='San Francisco')
    new_s.cities.append(new_c)
    session.add(new_s)
    session.add(new_c)
    session.commit()
