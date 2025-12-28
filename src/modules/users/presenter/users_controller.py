from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from common.database.db_helper import db_helper
import modules.users.domain.users_service as users_service

users_router = APIRouter(prefix="/users")


@users_router.get("/")
async def get_users(session: AsyncSession = Depends(db_helper.session_depedency)):
    return users_service.get_users(session=session)


@users_router.post("/{user_id}")
async def create_user(
    user_id: int, session: AsyncSession = Depends(db_helper.session_depedency)
):
    return users_service.get_user_by_id(session=session, user_id=user_id)
