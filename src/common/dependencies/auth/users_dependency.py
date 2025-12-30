from fastapi import Depends
from src.common.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.database.db_helper import db_helper


async def get_user_db(
    session: AsyncSession = Depends(db_helper.scoped_session_depedency),
):
    yield User.get_db(session)
