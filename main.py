
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from user.router import router as user_router
from room.router import router as room_router
from chat.router import router as chat_router
app = FastAPI()






@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient('mongodb+srv://gee:WC86EN6TT3K7cnyv@cluster0.ibe0l6m.mongodb.net/')
    app.mongodb = app.mongodb_client['aria_health']

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(user_router, tags=["users"], prefix="/user")
app.include_router(room_router, tags=["room"], prefix="/room")
app.include_router(chat_router, tags=["chat"], prefix="/chat")