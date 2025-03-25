from app import db
from app.models.user_model import User
from app.schemas.user import UserCreationData

from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users
    
    @staticmethod
    def create_user(data):
        try:
            user_data = UserCreationData(**data)
            new_user = User(name=user_data.name)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while creating a user: {str(e)}")
