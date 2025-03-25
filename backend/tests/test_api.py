import unittest
from app import create_app
from app.extensions import db

class TestAPI(unittest.TestCase):
    def setUp(self):
        """Set up the Flask app and application context."""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        """Tear down the application context and database."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_tasks(self):
        """Test GET /tasks/ endpoint."""
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        """Test POST /tasks/ endpoint."""
        response = self.client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        """Test GET /users/ endpoint."""
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """Test POST /users/ endpoint."""
        response = self.client.post("/users/", json={"name": "Test User"})
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()