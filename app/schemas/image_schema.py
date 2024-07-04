from pydantic import BaseModel,validator

class ImageSchema(BaseModel):
    id: int
    caption:str
 

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

@validator("caption")
def validate_caption(v):
    if not v:
        raise ValueError("caption cannot be empty")
    return v


