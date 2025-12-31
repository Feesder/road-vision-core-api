from fastapi import Depends
from src.modules.auth.manager.auth_manager import AuthManager
from src.common.dependencies.auth.users_dependency import get_users_db


async def get_auth_manager(users_db=Depends(get_users_db)):
    yield AuthManager(users_db)