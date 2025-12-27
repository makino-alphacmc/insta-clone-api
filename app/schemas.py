from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    image_url: str
    caption: str | None = None

  # リクエストスキーマ(必要あれば)
class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True