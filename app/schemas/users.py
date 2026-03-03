from pydantic import BaseModel , EmailStr
from typing import List, Annotated
from pydantic import Field
from datetime import datetime
from app.schemas.carts import CartBase


class UserBase(BaseModel):
    id: Annotated[int, Field(gt=0, description="The ID must be a positive integer.")]
    username: Annotated[str, Field(min_length=3, max_length=50, description="Username must be between 3 and 50 characters.")]
    email: Annotated[EmailStr, Field(..., description="The email address of the user.")]
    full_name: Annotated[str, Field(min_length=2, max_length=100, description="The full name of the user.")]
    password: Annotated[str, Field(min_length=6, max_length=100, description="The password of the user.")]
    role: Annotated[str, Field(..., description="The role of the user.")]
    is_active: Annotated[bool, Field(..., description="Indicates if the user is active.")]
    created_at: Annotated[datetime, Field(..., description="The date and time when the user was created.")]
    carts: Annotated[List[CartBase], Field(..., description="A list of carts associated with the user.")]



class UserCreate(BaseModel):
    full_name: Annotated[str, Field(min_length=2, max_length=100, description="The full name of the user.")]
    username: Annotated[str, Field(min_length=3, max_length=50, description="Username must be between 3 and 50 characters.")]
    email: Annotated[EmailStr, Field(..., description="The email address of the user.")]
    password: Annotated[str, Field(min_length=6, max_length=100, description="The password of the user.")]




class UserUpdate(UserCreate):
    pass


class UserOut(BaseModel):
    message: str
    data: UserBase


class UsersOut(BaseModel):
    message: str
    data: List[UserBase]


class UserOutDelete(BaseModel):
    message: str
    data: UserBase
