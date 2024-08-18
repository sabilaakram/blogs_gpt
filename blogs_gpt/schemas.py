from datetime import datetime
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str
    summary: str
    author: str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
