from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from .base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
