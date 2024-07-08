import bcrypt 

# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

def hashed_password(password:str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8')),
        return hashed_password

def verify_password(self,password:str):
    return bcrypt.checkpw(password.encode('utf-8'),self.hashed_password('utf-8'))