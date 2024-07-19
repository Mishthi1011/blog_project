from pydantic import BaseModel,validator,EmailStr
from app.models.users import User

class UserSchema(BaseModel):
    username:str
    email: EmailStr
    password: str
    contact:str
        

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

    @validator("contact")
    def validate_contact(v):
        if not v:
            raise ValueError("Phone Number cannot be empty")
        
        if len(v) > 10:
                raise ValueError("Phone Number cannot have more than 10 digits")
        return v