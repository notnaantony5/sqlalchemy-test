from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Base
engine = create_engine('sqlite:///test.db')

session_maker = sessionmaker(bind=engine)

with session_maker() as session:
    Base.metadata.create_all(engine)
    user2 = User(
        username="user2",
        first_name="John",
        last_name="Doe",
    )
    user3 = User(
        username="user3",
        first_name="John2",
        last_name="Doe2",
    )
    session.add_all([user2, user3])
    session.commit()

with session_maker() as session:
    user = session.query(User).filter(User.username == "user2").one()
    print(user.username, user.first_name, user.last_name, user.id)
    print("______")
    user.first_name = "John (updated)"
    session.commit()
    for user in session.query(User).all():
        print(user.username, user.first_name, user.last_name, user.id)



