#!/usr/bin/python3
"""List every state and the cities that belong to it."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()
    states = session.query(State).options(
        joinedload(State.cities)
    ).order_by(State.id).all()
    seen = set()
    for state in states:
        if state.id in seen:
            continue
        seen.add(state.id)
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda item: item.id):
            print("\t{}: {}".format(city.id, city.name))
    session.close()
