from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from src.common.dependencies.strategy import get_database_strategy 

bearer_transport = BearerTransport(
    tokenUrl="/api/v1/auth/sign-in",
)

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)