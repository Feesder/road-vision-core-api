from fastapi import APIRouter
from src.common.dependencies.auth.fastapi_users import fastapi_users
from src.common.dependencies.auth.auth_backend import authentication_backend

auth_router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend)
)