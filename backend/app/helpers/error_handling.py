from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

def register_error_handlers(app):
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({"error": str(e)}), 400

    @app.errorhandler(SQLAlchemyError)
    def handle_db_error(e):
        return jsonify({"error": "Database error occurred"}), 500