from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Annotated
from pydantic import Field
from app.schemas.carts import CartBase


class UserBase(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the user")]
    username: Annotated[str, Field(..., description="The username of the user")]
    email: Annotated[EmailStr, Field(..., description="The email address of the user")]
    full_name: Annotated[str, Field(..., description="The full name of the user")]
    password: Annotated[str, Field(..., description="The password of the user")]
    role: Annotated[str, Field(..., description="The role of the user, either 'admin' or 'user'")]
    is_active: Annotated[bool, Field(..., description="Indicates if the user is active")]
    created_at: Annotated[datetime, Field(..., description="The timestamp when the user was created")]
    carts: Annotated[List[CartBase], Field(..., description="A list of carts associated with the user")]


class Signup(BaseModel):
    full_name: Annotated[str, Field(..., description="The full name of the user")]
    username: Annotated[str, Field(..., description="The username of the user")]
    email: Annotated[EmailStr, Field(..., description="The email address of the user")]
    password: Annotated[str, Field(..., description="The password of the user")]
    role: Annotated[str, Field(..., description="The role of the user, either 'admin' or 'user'")]



class UserOut(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[UserBase, Field(..., description="The user data")]


# Token
class TokenResponse(BaseModel):
    access_token: Annotated[str, Field(..., description="The access token")]
    refresh_token: Annotated[str, Field(..., description="The refresh token")]
    token_type: Annotated[str, Field(..., description="The type of the token")] = 'Bearer'
    expires_in: int
