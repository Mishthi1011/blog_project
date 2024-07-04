from pydantic import BaseModel,validator

class BlogSchema(BaseModel):
    id: int
    title:str
    body: str
    image: str
    

@validator("id")
def validate_id(v):
    if not v:
        raise ValueError("Id cannot be empty")
    try:
            id_int = int(v)
            return id_int
    except ValueError:
            raise ValueError("Id must be an integer")
    r

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

@validator("image")
def validate_image(v):
    if not v:
        raise ValueError("Image is required")
    

