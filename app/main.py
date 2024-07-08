from fastapi import FastAPI, Body,HTTPException,status,Request
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse, Response, HTMLResponse
from app.database_connection.connection import *
from app.models import *
from app.schemas.user_schema import UserSchema
from app.schemas.blog_schema import BlogSchema
from app.schemas.image_schema import ImageSchema
from app.api.users import router as user_router
from app.api.blogs import router as blog_router
from app.api.images import router as image_router
import uvicorn
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.include_router(user_router)
app.include_router(blog_router)
app.include_router(image_router)



@app.exception_handler(HTTPException)
async def validation_exception_handler(request: Request, e: HTTPException):
    print.error(f"HTTPException Exception: {e}")
    return JSONResponse(
        status_code=e.status_code,
        content=jsonable_encoder({
            "success": False,
            "status_code":e.status_code,
            "error": f"{e.detail}"
        }),
    )