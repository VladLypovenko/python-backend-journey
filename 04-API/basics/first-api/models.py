from datetime import datetime

from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    title: str
    author: str
    created_at: datetime
    updated_at: datetime
