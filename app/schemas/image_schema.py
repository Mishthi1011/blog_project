from pydantic import BaseModel,validator
from app.models.images import Image

class ImageSchema(BaseModel):
    caption:str
    url:str

 
        
    @validator("url")
    def validate_url(v):
        if not v:
            raise ValueError("url cannot be empty")
        return v
    
    @validator("caption")
    def validate_caption(v):
        if not v:
            raise ValueError("caption cannot be empty")
        return v


