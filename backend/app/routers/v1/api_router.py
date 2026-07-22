from fastapi import APIRouter
from app.routers.v1 import upload, profile, clean, sql, chat

api_router = APIRouter()

api_router.include_router(upload.router)
api_router.include_router(profile.router)
api_router.include_router(clean.router)
api_router.include_router(sql.router)
api_router.include_router(chat.router)
