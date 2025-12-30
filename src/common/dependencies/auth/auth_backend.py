from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from src.common.dependencies.auth.strategy import get_database_strategy
from src.config.config import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.api_prefix.bearer_token_url,
)

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
