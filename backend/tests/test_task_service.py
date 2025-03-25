import unittest
from unittest.mock import patch
from app import create_app
from app.extensions import db
from app.models.task_model import Task, TaskStatus
from app.services.task_service import TaskService

class TestTaskService(unittest.TestCase):
    def setUp(self):
        """Set up the Flask app and application context."""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create a test database
        db.create_all()

    def tearDown(self):
        """Tear down the application context and database."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @patch("app.models.task_model.Task.query")
    def test_get_all_tasks(self, mock_query):
        """Test retrieving all tasks."""
        mock_query.all.return_value = [
            Task(id=1, title="Task 1", description="Description 1", status=TaskStatus.PENDING),
            Task(id=2, title="Task 2", description="Description 2", status=TaskStatus.COMPLETED),
        ]
        tasks = TaskService.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["title"], "Task 1")

    @patch("app.extensions.db.session")
    @patch("app.models.task_model.Task")
    def test_create_task(self, mock_task, mock_session):
        """Test creating a new task."""
        mock_task.return_value = Task(id=1, title="New Task", description="New Description", status=TaskStatus.PENDING)
        data = {"title": "New Task", "description": "New Description", "status": "pending"}
        task = TaskService.create_task(data)
        self.assertEqual(task.title, "New Task")
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()