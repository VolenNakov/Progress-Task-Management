from pydantic import BaseModel
from typing import Optional
from app.models.task_model import TaskStatus


class TaskCreationData(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    status: Optional[TaskStatus] = TaskStatus.PENDING


class TaskUpdatingData(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    status: Optional[TaskStatus] = None
