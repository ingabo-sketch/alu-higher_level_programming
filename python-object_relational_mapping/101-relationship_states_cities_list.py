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
    query = session.query(State).order_by(State.id)
    if hasattr(State.cities, "property"):
        query = query.options(joinedload(State.cities))
    seen = set()
    for state in query.all():
        if state.id in seen:
            continue
        seen.add(state.id)
        print("{}: {}".format(state.id, state.name))
        cities = sorted(state.cities, key=lambda city: city.id)
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
