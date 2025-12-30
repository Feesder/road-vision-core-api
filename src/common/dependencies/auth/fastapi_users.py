import uuid
from fastapi_users import FastAPIUsers
from src.common.dependencies.auth.auth_backend import authentication_backend
from src.common.dependencies.auth.auth_manager_dependency import get_user_manager
from src.common.models.user import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)