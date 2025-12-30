from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.database.db_helper import db_helper
from src.common.models.access_token import AccessToken


async def get_access_tokens_db(
    session: AsyncSession = Depends(db_helper.scoped_session_depedency),
):
    yield AccessToken.get_db(session)
