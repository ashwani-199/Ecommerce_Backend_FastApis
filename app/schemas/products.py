from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, ClassVar, Annotated
from app.schemas.categories import CategoryBase


class ProductBase(BaseModel):
    id: Annotated[int, Field(gt=0, description="The unique identifier of the product.")]
    title: Annotated[str, Field(min_length=2, max_length=200, description="The title of the product.")]
    description: Annotated[Optional[str], Field(max_length=500, description="The description of the product.")]
    price: Annotated[int, Field(gt=0, description="The price of the product.")]
    discount_percentage: Annotated[float, Field(ge=0, le=100, description="The discount percentage of the product.")]
    rating: Annotated[float, Field(ge=0, le=5, description="The rating of the product.")]
    stock: Annotated[int, Field(ge=0, description="The stock quantity of the product.")]
    brand: Annotated[str, Field(min_length=2, max_length=100, description="The brand of the product.")]
    thumbnail: Annotated[str, Field(min_length=5, max_length=200, description="The thumbnail URL of the product.")]
    images: Annotated[List[str], Field(description="A list of image URLs for the product.")]
    is_published: Annotated[bool, Field(description="Indicates whether the product is published.")]
    created_at: Annotated[datetime, Field(..., description="The date and time when the product was created.")]
    category_id: Annotated[int, Field(gt=0, description="The ID of the category to which the product belongs.")]
    category: Annotated[CategoryBase, Field(description="The category to which the product belongs.")]


# Create Product
class ProductCreate(ProductBase):
    id: Annotated[int, Field(gt=0, description="The unique identifier of the product.")]
    category: Annotated[CategoryBase, Field(description="The category to which the product belongs.")]

   


# Update Product
class ProductUpdate(ProductCreate):
    pass


# Get Products
class ProductOut(BaseModel):
    message: str
    data: ProductBase



class ProductsOut(BaseModel):
    message: str
    data: List[ProductBase]



# Delete Product
class ProductDelete(ProductBase):
    category: ClassVar[CategoryBase]


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete
