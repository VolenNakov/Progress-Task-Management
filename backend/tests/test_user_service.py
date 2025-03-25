import unittest
from unittest.mock import patch
from app import create_app
from app.extensions import db
from app.models.user_model import User
from app.services.user_service import UserService

class TestUserService(unittest.TestCase):
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

    @patch("app.models.user_model.User.query")
    def test_get_all_users(self, mock_query):
        """Test retrieving all users."""
        mock_query.all.return_value = [
            User(id=1, name="Alice"),
            User(id=2, name="Bob"),
        ]
        users = UserService.get_all_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "Alice")

    @patch("app.extensions.db.session")
    @patch("app.models.user_model.User")
    def test_create_user(self, mock_user, mock_session):
        """Test creating a new user."""
        mock_user.return_value = User(id=1, name="Charlie")
        data = {"name": "Charlie"}
        user = UserService.create_user(data)
        self.assertEqual(user.name, "Charlie")
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()