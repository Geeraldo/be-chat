from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import RoomModel

router = APIRouter()


@router.post("/", response_description="Add new Room")
async def create_room(request: Request, room:RoomModel = Body(...)):
    room = jsonable_encoder(room)
    new_room = await request.app.mongodb["room"].insert_one(room)
    created_room = await request.app.mongodb["user"].find_one(
        {"_id": new_room.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_room)


@router.get("/", response_description="List all Room")
async def list_room(request: Request):
    rooms = []
    for doc in await request.app.mongodb["room"].find().to_list(length=100):
        rooms.append(doc)
    return rooms


@router.get("/join/{id}", response_description="Join Room")
async def detail_user(id: str, request: Request):
    if (user := await request.app.mongodb["user"].find_one({"_id": id})) is not None:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")
