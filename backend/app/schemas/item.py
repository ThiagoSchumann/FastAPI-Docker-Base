from typing import Optional
from sqlmodel import SQLModel, Field

class ItemBase(SQLModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int
    owner_id: int

class ItemUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
