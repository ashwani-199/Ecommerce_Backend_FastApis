from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Annotated
from pydantic import Field
from app.schemas.carts import CartBase


class AccountBase(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the account")]
    username: Annotated[str, Field(..., description="The username of the account")]
    email: Annotated[EmailStr, Field(..., description="The email address of the account")]
    full_name: Annotated[str, Field(..., description="The full name of the account")]
    role: Annotated[str, Field(..., description="The role of the account")]
    is_active: Annotated[bool, Field(..., description="Indicates if the account is active")]
    created_at: Annotated[datetime, Field(..., description="The timestamp when the account was created")]
    carts: Annotated[List[CartBase], Field(..., description="A list of carts associated with the account")]


class AccountUpdate(BaseModel):
    username: Annotated[str, Field(..., description="The username of the account")]
    email: Annotated[EmailStr, Field(..., description="The email address of the account")]
    full_name: Annotated[str, Field(..., description="The full name of the account")]


class AccountOut(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[AccountBase, Field(..., description="The account data")] = None


