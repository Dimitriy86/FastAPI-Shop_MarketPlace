from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity(must be greater than 0)")


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity(must be greater than 0)")


class CartItem(BaseModel):
    product_id: int
    name: str
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Total price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: int = Field(..., description="Total number of items in cart")
    items_count: int = Field(..., description="Number of items in cart")
