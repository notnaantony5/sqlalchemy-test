from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Base, Task, Priority

engine = create_engine('sqlite:///test.db')

session_maker = sessionmaker(bind=engine)

def main():
    while True:
        try:
            priority = int(
                input('Введите приоритет для вывода (1-3): ')
            )
            if priority < 1 or priority > 3:
                raise ValueError
        except ValueError:
            print("Ошибка, повторите ввод!")
        else:
            break
    # priority = int(input('Введите приоритет для вывода (1-3): '))
    with session_maker() as session:
        tasks = session.query(Task).filter(
            Task.priority == Priority(priority)
        ).all()
        for task in tasks:
            print(task.to_representation())
if __name__ == '__main__':
    main()





