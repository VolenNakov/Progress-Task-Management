from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

api = Api(version="0.1", title="Task Management API")
db = SQLAlchemy()
cors = CORS()
