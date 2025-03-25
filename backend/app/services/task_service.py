from app.extensions import db
from app.models.task_model import Task, TaskStatus
from app.models.user_model import User
from app.schemas.task import TaskCreationData, TaskUpdatingData
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError


class TaskService:
    @staticmethod
    def get_all_tasks():
        tasks = Task.query.all()
        return [task.to_dict() for task in tasks]

    @staticmethod
    def create_task(data: dict) -> Task:
        try:
            task_data = TaskCreationData(**data)

            if task_data.assigned_to:
                user = User.query.get(task_data.assigned_to)
                if not user:
                    raise ValueError("Assigned user does not exist")
                
            if task_data.status not in TaskStatus:
                 raise ValueError("Invalid task status")

            new_task = Task(
                title=task_data.title,
                description=task_data.description,
                assigned_to=task_data.assigned_to,
                status=task_data.status,
            )

            db.session.add(new_task)
            db.session.commit()
            return new_task
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while creating a task: {str(e)}")

    @staticmethod
    def update_task(task_id: int, data: dict) -> Task:
        task = Task.query.get(task_id)
        if not task:
            raise ValueError("Task not found")

        try:
            task_data = TaskUpdatingData(**data)

            if task_data.title is not None:
                task.title = task_data.title
            if task_data.description is not None:
                task.description = task_data.description
            if task_data.assigned_to is not None:
                user = User.query.get(task_data.assigned_to)
                if not user:
                    raise ValueError("Assigned user does not exist")
                task.assigned_to = task_data.assigned_to
            if task_data.status is not None:
                task.status = task_data.status

            db.session.commit()
            return task
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while updating the task: {str(e)}")

    @staticmethod
    def assign_task(task_id: int, user_id: int) -> Task:
        task = Task.query.get(task_id)
        if not task:
            raise ValueError("Task not found")

        user = User.query.get(user_id)
        if not user:
            raise ValueError("Assigned user not found")

        try:
            task.assigned_to = user_id
            db.session.commit()
            return task
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")

    @staticmethod
    def delete_task(task_id: int):
        task = Task.query.get(task_id)
        if not task:
            raise ValueError("Task not found")

        try:
            db.session.delete(task)
            db.session.commit()
            return task
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while deleting the task: {str(e)}")
