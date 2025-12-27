from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    image_url: str