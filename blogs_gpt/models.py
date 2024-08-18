from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    summary: str
    content: str
    author: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
