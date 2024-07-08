from fastapi import APIRouter,HTTPException
from app.schemas.image_schema import ImageSchema
from fastapi.responses import JSONResponse
from app.models.images import Image
from app.database_connection.connection import db

router = APIRouter(prefix="/api/v1/images",tags=["image API's"])

@router.post("",summary="posted an image",description="posts an image by using imageschema information")
def create_image(image:ImageSchema):
    """
    Posts image by using information given by user
    Args:
        image(Imageschema):posts image by using imageschem information
    Returns:
        It reurns jasonresponse
    """
    try:
        image_info = dict(image)
        save_image = image(**image_info)
        db.add(save_image)
        db.commit()
        return JSONResponse(content={"message":"image has been posted to blog ","data":[]},status_code=201)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)
   


@router.get("")
def get_image_details():
    try:    
        images = db.query(Image).all()
        print(images ,"333")
        all_images = [obj.info() for obj in images]
        return JSONResponse(content={"message":"data fetched","data":all_images},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)

  
@router.put("/{id}")
def update_image_status(id:int, updateImage:ImageSchema):
    try:
        image = db.query(Image).get(id)
        image.url = updateImage.url
        image.caption = updateImage.caption
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":image},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)    

@router.delete("/{id}")
def delete_image(id:int):
    try:
        image = db.query(Image).get(id)
        db.delete(image)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":image},status_code=200)    
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"user not found","data":[]}, status_code=404)