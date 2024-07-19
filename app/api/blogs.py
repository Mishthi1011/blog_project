from fastapi import APIRouter, Depends,HTTPException,Body, Request,Form
from app.auth.dependencies import get_current_user
from app.schemas.blog_schema import BlogSchema
from fastapi.responses import JSONResponse,RedirectResponse,HTMLResponse
from app.models.blogs import Blog
from app.database_connection.connection import db
from datetime import datetime

router = APIRouter (prefix="/api/v1/blogs",tags=["blog API's"])

@router.post("",summary="created a blog",description="creates blog by using blogschema information")
def create_blog(blog:BlogSchema, current_user: str = Depends(get_current_user)):
    """
    Create blog by using information given by user
    Args:
        blog(Blogschema): creates blog by using blogschema information
    Returns:
        It returns jsonresponse    
    """
    try:
        print(current_user , "##########current user")
        blog_info = dict(blog)
        print(blog_info, "#######bloginfo")
        blog_info['created_at'] = datetime.now()
        blog_info['user_id'] = current_user
        save_blog = Blog(**blog_info)
        db.add(save_blog)
        db.commit()
        return JSONResponse(content={"message":"blog created by user","data":[]},status_code=201)
    except Exception as e:
        print(e ,"##########")
        db.rollback()
        return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)


@router.put("/{id}")
def update_blog_status(id:int,updateBlog:BlogSchema,current_user: str = Depends(get_current_user)):
    
        print(current_user , "##########current user")
        blog = db.query(Blog).get(id)
        if blog.user_id == current_user:
            print(id ,updateBlog.title, "######")
            blog.title = updateBlog.title
            blog.body = updateBlog.body
            blog.image_url = updateBlog.image_url
        
            db.commit()
            return JSONResponse(content={"message":"data fetched","data":[]},status_code=200)
        
        else:
            return JSONResponse(content = {"message":"blog can't be updated","data":[]},status_code=203)
        
    
@router.delete("/{id}")
def delete_user(id:int,):
     try:
       
        blog = db.query(Blog).get(id)
       
        db.delete(blog)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":blog},status_code=200)
     except Exception as e:
         print(e ,"##########")
         db.rollback()
         return JSONResponse(content={"message":"blog not found","data":[]}, status_code=404)    
    
 

@router.post("/blog")
async def post_create_blog(
    title: str = Form(...),
    content: str = Form(...),
    image_url: str = Form(...),
    
    
):
    blog = Blog(title=title, content=content,image_url=image_url)
    
    blog_id = len(Blog) + 1

    Blog[blog_id] = blog.dict()
    
    
    return {"message": "Blog created successfully!", "blog_id": blog_id,}



