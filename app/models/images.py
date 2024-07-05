from app.database_connection.connection import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func,ForeignKey,Text,URL
from app.models.users import User
from app.models.blogs import Blog

class Image(Base):
       __tablename__ = "images"
       id = Column(Integer, primary_key=True, autoincrement=True)
       blog_id = Column(Integer,autoincrement=True)
       blog  = ForeignKey("blogs", backref="images")
       created_at = Column(DateTime,nullable=False)
       updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
       url = Column(String(100))
       caption = Column(String(100))

       def info(self):
        return({
            "id": self.id,
            "url":self.url,
            "caption":self.caption,
        })