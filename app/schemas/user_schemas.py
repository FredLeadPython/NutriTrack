from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int


class UserResult(BaseModel):
    id: UUID
    username: str
    email: str
    age: int
