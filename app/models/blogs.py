from app.database_connection.connection import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func,ForeignKey,Text
from sqlalchemy.orm import relationship
from app.models.users import User

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"),autoincrement=True)
    user = ForeignKey("users", backref="blogs")
    title = Column(String(100))
    body = Column(Text)
    created_at = Column(DateTime,nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    image = Column(String(200))

    def info(self):
        return({
            "id": self.id,
            "title":self.title,
            "body":self.body,
            
        })