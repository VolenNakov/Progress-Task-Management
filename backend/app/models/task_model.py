from app.extensions import db
import enum


class TaskStatus(enum.Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer, db.ForeignKey("users.id"))
    status = db.Column(db.Enum(TaskStatus))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "status": self.status.value,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


def __init__(self, title, description, created_by, assigned_to, status):
    self.title = title
    self.description = description
    self.created_by = created_by
    self.assigned_to = assigned_to
    self.status = status
