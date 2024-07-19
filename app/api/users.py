from fastapi import APIRouter, HTTPException,Body,Form
from app.schemas.user_schema import UserSchema
from fastapi.responses import JSONResponse,RedirectResponse
from app.models.users import User
from app.database_connection.connection import db
from app.helper_functions.hashing import hashed_password
from app.helper_functions.auth import check_user_creds
from app.auth.dependencies import *

router = APIRouter(prefix="/api/v1/users",tags=["user API's"])

@router.post("", summary="created users", description="it creates user by using userschema information")
def create_user(user:UserSchema):
    """
    Create user by using user information
    Args:
        user (Userschema): It create user by using userschema information

    Returns:
        It returns jsonreponse
    """
    try:
        user_info = dict(user)
        save_user = User(**user_info)
        db.add(save_user)
        db.commit()
        return JSONResponse(content={"message":"account created successfully","data":[]},status_code=201)
    except Exception as e:
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)

@router.get("")
def get_user_details():
    try:
        users = db.query(User).all()
        print(users ,"111")
        all_users = [obj.info() for obj in users]
        return JSONResponse(content={"message":"data fetched","data":all_users},status_code=200)
    except Exception as e:
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)
            
@router.put("/{id}")
def update_user_status(id:int, updateUser:UserSchema =Body()):
    try:
        user = db.query(User).get(id)
        user.email = updateUser.email
        user.username = updateUser.username
        user.contact = updateUser.contact
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":user},status_code=200)
    except Exception as e:
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)

@router.delete("/{id}")
def delete_user(id:int):
    try:
        user = db.query(User).get(id)
        db.delete(user)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":user},status_code=200)       
    except Exception as e:
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)    
    
@router.post("/blog")
async def post_register(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    contact: str = Form(...),
):
    return JSONResponse(content={"message": "User registered successfully!"},status_code=200) 
    return RedirectResponse(url="/blog", status_code=303) 
  
@router.post("/login") 
async def login_register(
    userCreds: dict = Body(...),
):
    print(userCreds['username'], userCreds['password'], type(userCreds) , "######usercreds")
    user_check = check_user_creds(userCreds['username'],userCreds['password'])
    print(user_check , "####apicheck")
    
    if user_check is not None:
        token = create_access_token({"id":user_check.id})
        print(token , "######token ")
        return JSONResponse(content={"message":"logged in","token":token,"token_type":"bearer","data":[]}, status_code=200)
    else:
        return JSONResponse(content={"message":"User creds are incorrect"},status_code=401)
    