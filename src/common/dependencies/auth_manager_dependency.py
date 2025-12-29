from fastapi import Depends
from src.modules.auth.manager.auth_manager import AuthManager
from src.common.dependencies.users_dependency import get_user_db

async def get_user_manager(user_db=Depends(get_user_db)):
    yield AuthManager(user_db)