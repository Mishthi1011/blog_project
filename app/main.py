from fastapi import FastAPI, Body,HTTPException,status,Request,Form
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from app.database_connection.connection import *
from app.models.users import *
from app.models.blogs import *
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from app.schemas import *
from app.api.users import router as user_router
from app.api.blogs import router as blog_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.exception_handler(HTTPException)
# async def validation_exception_handler(request: Request, e: HTTPException):
#     print.error(f"HTTPException Exception: {e}")
#     return JSONResponse(
#         status_code=e.status_code,
#         content=jsonable_encoder({
#             "success": False,
#             "status_code":e.status_code,
#             "error": f"{e.detail}"
#         }),
#     )


@app.get("/register", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/blog")
async def get_blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/option")
async def get_option(request :Request):
    return templates.TemplateResponse("option.html",{"request":request})



@app.get("/all_blogs")
def get_user_details(request:Request):
    from app.main import templates
    try:
        blogs = db.query(Blog).all()
        
        all_bloggs = [obj.info() for obj in blogs]
        return templates.TemplateResponse("user_blogs.html", {"request": request,"data":all_bloggs})
        
    except Exception as e:  
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)



app.include_router(user_router)
app.include_router(blog_router)


