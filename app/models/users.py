from app.database_connection.connection import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func,ForeignKey
i

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False) 
    hashed_password = Column(String(255), nullable=False) 
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    contact = Column(Integer,unique=True, nullable=False)

    def info(self):
        return({
            "id": self.id,
            "username":self.username,
            "email":self.email,
            "contact":self.contact
        })

    
    

