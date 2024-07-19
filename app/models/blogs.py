from app.database_connection.connection import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func,ForeignKey,Text
from sqlalchemy.orm import relationship
from app.models.users import User

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = ForeignKey("users", backref="blogs")
    title = Column(String(100))
    body = Column(Text)
    image_url = Column(String(100))
    created_at = Column(DateTime,nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
  

    def info(self):
        return({
            "id": self.id,
            "user_id":self.user_id,
            "title":self.title,
            "body":self.body,
            "image_url":self.image_url,
        
        })