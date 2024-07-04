from pydantic import BaseModel,validator,EmailStr
from models.users import User

class UserSchema(BaseModel):
    id: int
    username:str
    email: EmailStr
    password: str
    phone_number:int

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

@validator("username")
def validate_username(v):
    if not v:
        raise ValueError("Username cannot be empty")
    if len(v) > 15:
             raise ValueError("Username length must not exceed 15 characters")
    if ' ' in v:
            raise ValueError("Username cannot contain spaces.")
    return v


@validator("email")
def validate_email(v):
    if not v:
        raise ValueError("Email cannot be empty")
    if ' ' in v:
            raise ValueError("Email cannot contain spaces.")
    return v

@validator("password")
def validate_password(v):
    if not v:
        raise ValueError("Password cannot be empty")
    if ' ' in v:
            raise ValueError("Password cannot contain spaces.")
    return v

@validator("phone_number")
def validate_phone_number(v):
    if not v:
        raise ValueError("Phone Number cannot be empty")
    if ' ' in v:
            raise ValueError("Phone number cannot contain spaces.")
    if len(v) > 10:
             raise ValueError("Phone Number cannot have more than 10 digits")
    return v