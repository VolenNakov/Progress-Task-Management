import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
