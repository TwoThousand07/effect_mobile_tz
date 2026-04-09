import bcrypt
import jwt

from datetime import datetime, timedelta
from decouple import config

SECRET_KEY: str = config("SECRET_KEY")


def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password: str, hashed: str):
    return bcrypt.checkpw(password.encode(), hashed.encode())


def create_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.now() + timedelta(days=1)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return None
