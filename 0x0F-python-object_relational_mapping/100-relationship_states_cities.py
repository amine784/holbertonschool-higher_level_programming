#!/usr/bin/python3
''' script that def state'''
if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import Session, relationship
    import sys
    from sqlalchemy import create_engine
    from relationship_state import Base, State, City
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db))
    Base.metadata.create_all(engine)
    session = Session(engine)
    '''p = State(name="California")
    session.add(p.cities.append(City(name="San Francisco")))'''
    x = State(name='California')
    y = City(name='San Francisco')
    x.cities.append(y)
    session.commit()
    session.close()
