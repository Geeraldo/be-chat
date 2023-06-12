import uuid
from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    token: str =Field(default_factory=uuid.uuid5)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0ddedw220e0f",
                "name": "Danica",
                "token": "083823-efewfwe2-adefef",
            }
        }


class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "My other important task",
                "completed": True,
            }
        }