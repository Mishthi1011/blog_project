from app.models.users import User
from app.database_connection.connection import db


def check_user(user):
    user_exists = db.query(User).get(user.id)
    if user_exists:
        return user_exists
    else:
        return None

def check_user_creds(username,password):
    user_check = db.query(User).filter_by(username=username,password=password).all()
    if len(user_check) != 0:
        return user_check[0]
    return None