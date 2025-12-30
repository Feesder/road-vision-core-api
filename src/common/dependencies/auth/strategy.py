from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import AccessTokenDatabase
from src.common.models.access_token import AccessToken
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from src.common.models.access_token import AccessToken
from src.config.config import settings
from src.common.dependencies.auth.access_tokens_dependency import get_access_tokens_db


def get_database_strategy(
    access_tokens_db: AccessTokenDatabase[AccessToken] = Depends(get_access_tokens_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_tokens_db, settings.access_token_settings.access_token_expire
    )
