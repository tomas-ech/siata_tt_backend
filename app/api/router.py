from fastapi import APIRouter
from app.api.endpoints import users, delivery, auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])

api_router.include_router(users.router, prefix="/users", tags=["Users"])

api_router.include_router(delivery.router, prefix="/delivery", tags=["Delivery"])
