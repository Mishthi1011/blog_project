from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse, Response, HTMLResponse
from app.database_connection.connection import *
from app.models import *
from app.models.users import User
from app.models.images import Blog
from app.models.images import Image
import uvicorn
app = FastAPI()

@app.post("/")
def users(body:dict = Body(...)):
    email = body.get("email")
    username = body.get("username")
    password = body.get("password")
    phone_number = body.get("phone_number")
    user = User(email=email, username=username, password=password, phone_number=phone_number)
    db.add(user)
    db.commit()
    return JSONResponse(content={user.info()}, status_code=200)

def blogs(body:dict = Body(...)):
    title = body.get("title")
    body = body.get("body")
    blog = Blog(title=title, body=body)
    db.add(blog)
    db.commit()
    return JSONResponse(content={blog.info()}, status_code=200)

def images(body:dict = Body(...)):
    caption = body.get("caption")
    image = Image(caption=caption)
    db.add(image)
    db.commit()
    return JSONResponse(content={image.info()}, status_code=200)

