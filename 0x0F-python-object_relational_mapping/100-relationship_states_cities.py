#!/usr/bin/python3
''' script that def state'''
if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import Session
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from relationship_city import City
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db))
    Base.metadata.create_all(engine)
    session = Session(engine)
    p = State(name="California")
    session.add(p.cities.append(City(name="San Francisco")))
    session.commit()
    session.close()
