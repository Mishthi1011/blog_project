import bcrypt 

def hashed_password(password:str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8')),
        return hashed_password

def verify_password(self,password:str):
    return bcrypt.checkpw(password.encode('utf-8'),self.hashed_password('utf-8'))