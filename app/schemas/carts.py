from pydantic import BaseModel, Field
from typing import List, Annotated
from datetime import datetime
from app.schemas.products import ProductBase, CategoryBase


class ProductBaseCart(ProductBase):
    category: Annotated[CategoryBase, Field(..., description="The category of the product")]



# Base Cart & Cart_Item
class CartItemBase(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the cart item")]
    product_id: Annotated[int, Field(..., description="The unique identifier of the product")]
    quantity: Annotated[int, Field(..., description="The quantity of the product in the cart")]
    subtotal: Annotated[float, Field(..., description="The subtotal for the cart item")]
    product: Annotated[ProductBaseCart, Field(..., description="The product associated with the cart item")]

class CartBase(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the cart")]
    user_id: Annotated[int, Field(..., description="The unique identifier of the user")]
    created_at: Annotated[datetime, Field(..., description="The timestamp when the cart was created")]
    total_amount: Annotated[float, Field(..., description="The total amount of the cart")]
    cart_items: Annotated[List[CartItemBase], Field(..., description="A list of cart items")]



class CartOutBase(BaseModel):
    id: Annotated[int, Field(..., description="The unique identifier of the cart")]
    user_id: Annotated[int, Field(..., description="The unique identifier of the user")]
    created_at: Annotated[datetime, Field(..., description="The timestamp when the cart was created")]
    total_amount: Annotated[float, Field(..., description="The total amount of the cart")]
    cart_items: Annotated[List[CartItemBase], Field(..., description="A list of cart items")]




# Get Cart
class CartOut(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[CartOutBase, Field(..., description="The cart data")]


class CartsOutList(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[List[CartOutBase], Field(..., description="A list of cart data")]


class CartsUserOutList(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[List[CartOutBase], Field(..., description="A list of cart data")]

   


# Delete Cart
class CartOutDelete(BaseModel):
    message: Annotated[str, Field(..., description="A message indicating the result of the operation")]
    data: Annotated[CartOutBase, Field(..., description="The deleted cart data")]


# Create Cart
class CartItemCreate(BaseModel):
    product_id: Annotated[int, Field(..., description="The unique identifier of the product")]
    quantity: Annotated[int, Field(..., description="The quantity of the product in the cart")]


class CartCreate(BaseModel):
    cart_items: Annotated[List[CartItemCreate], Field(..., description="A list of cart items")]

 

# Update Cart
class CartUpdate(CartCreate):
    pass
