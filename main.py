from fastapi import FastAPI
from routes.user import router as user_router
from routes.auth import router as auth_router

app = FastAPI()
app.include_router(user_router, prefix="/user")
app.include_router(auth_router, prefix="/auth")
