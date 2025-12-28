from common.models.user import User
from modules.users.dto.user_dto import UserDto


def map_user_model_to_dto(user_model: User) -> UserDto:
    return UserDto(
        username=user_model.username,
        email=user_model.email,
    )
