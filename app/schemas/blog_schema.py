from pydantic import BaseModel,validator
from app.models.blogs import Blog

class BlogSchema(BaseModel):
    title:str
    body: str
    image_url: str
   
    @validator("title")
    def validate_title(v):
        if not v:
            raise ValueError("Title cannot be empty")
        if len(v) > 50:
                raise ValueError("Title length must not exceed 50 characters")
        return v


    @validator("body")
    def validate_body(v):
        if not v:
            raise ValueError("Body cannot be empty")
        return v

    @validator("image_url")
    def validate_image_url(v):
        if not v:
            raise ValueError("url cannot be empty")
        return v


