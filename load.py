from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task, Priority

engine = create_engine('sqlite:///test.db')

session_maker = sessionmaker(bind=engine)
with session_maker() as session:
    Base.metadata.create_all(engine)
    tasks = [
        Task(
            title='Task 1',
            description='Task 1',
            priority=Priority.HIGH,
        ), Task(
            title='Task 2',
            description='Task 2',
            priority=Priority.HIGH,
        ), Task(
            title='Task 3',
            description='Task 3',
            priority=Priority.LOW,
        )
    ]
    session.add_all(tasks)
    session.commit()
