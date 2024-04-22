from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, lazyload, selectinload, joinedload
from models import Base, Message, User

engine = create_engine('sqlite:///test.db', echo=True)

session_maker = sessionmaker(bind=engine)
LOAD = False
if LOAD:
    with session_maker() as session:
        Base.metadata.create_all(engine)
        sasha = User(username="sasha")
        petya = User(username="petya")
        sasha_messages = [Message(user=sasha, text="sasha1"),
                          Message(user=sasha, text="sasha2")]
        petya_messages = [Message(user=petya, text="petya1"),
                          Message(user=petya, text="petya2")]
        session.add_all([sasha, petya, *sasha_messages, *petya_messages])
        session.commit()

with session_maker() as session:
    sql = text("SELECT users.id AS users_id, users.username AS users_username, messages_1.id AS messages_1_id, messages_1.text AS messages_1_text, messages_1.user_id AS messages_1_user_id "
"FROM users LEFT OUTER JOIN messages AS messages_1 ON users.id = messages_1.user_id")

    result = engine.connect().execute(sql)
    for row in result:
        print(row)
    print("____________________________________")
    sql = text("""SELECT users.id AS users_id, users.username AS users_username
FROM users""")
    result = engine.connect().execute(sql)
    for row in result:
        print(row)
    print("********")
    sql = text("""SELECT messages.user_id AS messages_user_id, messages.id AS messages_id, messages.text AS messages_text
FROM messages
WHERE messages.user_id IN (1, 2)""")
    result = engine.connect().execute(sql)
    for row in result:
        print(row)
    print("____________________________________")
    users = session.query(User).options(selectinload(User.messages)).all()
    print(users)
    for user in users:
        print(user.username)
        for message in user.messages:
            print(message.text)
    print()
