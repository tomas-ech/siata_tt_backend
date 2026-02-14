from fastapi import APIRouter
from app.api.endpoints import users, delivery

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(delivery.router, prefix="/delivery", tags=["Delivery"])