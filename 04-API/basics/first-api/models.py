from datetime import datetime

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    created_at: datetime
    updated_at: datetime
