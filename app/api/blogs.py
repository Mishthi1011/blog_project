from fastapi import APIRouter,HTTPException
from app.schemas.blog_schema import BlogSchema
from fastapi.responses import JSONResponse
from app.models.blogs import Blog
from app.database_connection.connection import db

router = APIRouter(prefix="/api/v1/blogs",tags=["blog API's"])

@router.post("",summary="created a blog",description="creates blog by using blogschema information")
def create_blog(blog:BlogSchema):
    """
    Create blog by using information given by user
    Args:
        blog(Blogschema): creates blog by using blogschema information
    Returns:
        It returns jsonresponse    
    """
    try:
        blog_info = dict(blog)
        save_blog = Blog(**blog_info)
        db.add(save_blog)
        db.commit()
        return JSONResponse(content={"message":"blog created by user","data":[]},status_code=201)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)

@router.get("")
def get_user_details():
    try:
        blogs = db.query(Blog).all()
        print(blogs ,"222")
        all_blogs = [obj.info() for obj in blogs]
        return JSONResponse(content={"message":"data fetched","data":all_blogs},status_code=200)
    except Exception as e:  
        print(e ,"##########")
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)
     

@router.put("/{id}")
def update_blog_status(id:int, updateBlog:BlogSchema):
    try:
        blog = db.query(Blog).get(id)
        blog.title = updateBlog.title
        blog.body = updateBlog.body
        blog.status = updateBlog.status
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":blog},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)

@router.delete("/{id}")
def delete_user(id:int):
    try:    
        blog = db.query(Blog).get(id)
        # blog.title = Blog.title
        # blog.body = Blog.body
        # blog.status = Blog.status
        db.delete(blog)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":blog},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)    