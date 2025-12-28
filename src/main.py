from fastapi import FastAPI

from src.modules.auth.presenter.auth_controller import auth_router
from src.modules.users.presenter.users_controller import users_router

app = FastAPI(title="Road Vision Core API")
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
