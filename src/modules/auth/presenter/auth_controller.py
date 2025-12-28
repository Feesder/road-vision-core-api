from fastapi import APIRouter

auth_router = APIRouter(prefix="/api/v1/auth")


@auth_router.post("/sign-up")
def signUp():
    pass


@auth_router.post("/sign-in")
def singIn():
    pass


@auth_router.post("/sign-out")
def signOut():
    pass


@auth_router.post("/refresh")
def refresh():
    pass
