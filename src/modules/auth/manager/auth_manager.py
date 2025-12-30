import logging
from typing import Optional
import uuid
from fastapi import Request
from fastapi_users.manager import BaseUserManager, UUIDIDMixin
from src.common.models.user import User
from src.config.config import settings

log = logging.getLogger(__name__)


class AuthManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = (
        settings.access_token_settings.reset_password_token_secret
    )
    verification_token_secret = (
        settings.access_token_settings.verification_token_secret
    )

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %s has registered.", user.id)

    # async def on_after_forgot_password(
    #     self, user: User, token: str, request: Optional[Request] = None
    # ):
    #     log.warning(
    #         "User %s has forgot their password. Reset token: %s", user.id, token
    #     )

    # async def on_after_request_verify(
    #     self, user: User, token: str, request: Optional[Request] = None
    # ):
    #     log.warning(
    #         "Verification requested for user %s. Verification token: %s", user.id, token
    #     )
