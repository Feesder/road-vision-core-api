import asyncio
import contextlib
from os import getenv

from src.common.dependencies.auth.users_dependency import get_users_db
from src.modules.auth.presenter.schemas.user_schema import UserCreate
from src.common.dependencies.auth.auth_manager_dependency import get_auth_manager
from fastapi_users.exceptions import UserAlreadyExists
from src.common.database.db_helper import db_helper

get_user_db_context = contextlib.asynccontextmanager(get_users_db)
get_auth_manager_context = contextlib.asynccontextmanager(get_auth_manager)


default_email = getenv("SUPERUSER_EMAIL", "admin@example.com")
default_username = getenv("SUPERUSER_USERNAME", "admin")
default_password = getenv("SUPERUSER_PASSWORD", "12345")
default_is_superuser = True
default_is_active = True
default_is_verified = True


async def create_superuser(email:str=default_email,
                           password:str=default_password,
                           username:str=default_username,
                           is_superuser:bool=default_is_superuser,
                           is_active:bool=default_is_active,
                           is_verified:bool=default_is_verified):
    try:
        async with db_helper.scoped_session_depedency() as session:
            async with get_user_db_context(session) as user_db:
                async with get_auth_manager_context(user_db) as auth_manager:
                    user = await auth_manager.create(
                        UserCreate(
                            email=email, password=password, is_superuser=is_superuser, username=username, is_active=is_active, is_verified=is_verified
                        )
                    )
                    return user
    except UserAlreadyExists:
        raise


if __name__ == "__main__":
    asyncio.run(create_superuser())