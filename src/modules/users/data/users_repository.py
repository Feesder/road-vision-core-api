from sqlalchemy import select
from sqlalchemy.engine import Result
from common.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from modules.users.dto.user_dto import CreateUserDto


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, payload: CreateUserDto) -> User:
    user = User(**payload.dict())
    session.add(user)
    await session.commit()
    return user
