from typing import List, Annotated
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: Annotated[int, Field(readOnly=True)]
    name: Annotated[str, Field(..., description="The name of the category")]


class CategoryCreate(BaseModel):
    name: Annotated[str, Field(..., description="The name of the category")]


class CategoryUpdate(BaseModel):
    name: Annotated[str, Field(..., description="The name of the category")]


class CategoryOut(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[CategoryBase, Field(..., description="The category data")]


class CategoriesOut(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[List[CategoryBase], Field(..., description="A list of category data")]


class CategoryDelete(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the category")]
    name: Annotated[str, Field(..., description="The name of the category")]


class CategoryOutDelete(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[CategoryDelete, Field(..., description="The deleted category data")]
