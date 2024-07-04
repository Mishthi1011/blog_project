from app.models import users, images, blogs
from app.database_connection.connection import Base, engine

Base.metadata.create_all(bind=engine)