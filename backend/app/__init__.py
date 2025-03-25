from flask import Flask
from app.extensions import api, db, cors
from app.config.config import Config
from app.helpers.error_handling import register_error_handlers
from app.controllers.task_controller import task_ns
from app.controllers.user_controller import user_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_error_handlers(app)

    db.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    api.add_namespace(task_ns, "/tasks")
    api.add_namespace(user_ns, "/users")

    @app.cli.command("init-db")
    def init_db():
        """Initialize the database."""
        db.create_all()
        print("Database initialized!")

    return app
