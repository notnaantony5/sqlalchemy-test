import datetime
import enum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Priority(enum.Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Base(DeclarativeBase):
    __abstract__ = True


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    priority: Mapped[Priority]

    def to_representation(self) -> str:
        return (f"Задача id={self.id}\n"
                f"{self.title}\n"
                f"{self.description}\n"
                f"Приоритет - {self.priority.value}\n")
