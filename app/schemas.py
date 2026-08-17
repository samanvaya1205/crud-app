from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    description:Optional[str] = None
    price: Decimal
    in_stock: bool = True

class ItemResponse(BaseModel):
    id: int
    name: str
    description:Optional[str]
    price: Decimal
    in_stock: bool
    created_at: datetime

    class Config:
        from_attributes = True