import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/m608db")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "m608db")
