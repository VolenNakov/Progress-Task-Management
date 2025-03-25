from flask_restx import Namespace, Resource, fields
from app.services.task_service import TaskService

task_ns = Namespace("tasks", "Task operations")

# This model is what the api should return and this is why we have 1 model in the controller and
# another one in the models folder
task_model = task_ns.model(
    "Task",
    {
        "id": fields.Integer(readonly=True),
        "title": fields.String(readonly=True),
        "description": fields.String(readonly=True),
        "created_at": fields.String(readonly=True),
        "assigned_to": fields.Integer(readonly=True),
        "status": fields.String(readonly=True),
    },
)


@task_ns.route("/")
class TaskList(Resource):
    @task_ns.marshal_list_with(task_model)
    def get(self):
        """Get all tasks"""
        return TaskService.get_all_tasks()

    @task_ns.marshal_with(task_model, code=201)
    @task_ns.expect(task_model, validate=True)
    def post(self):
        """Create a task"""
        return TaskService.create_task(task_ns.payload), 201


@task_ns.route("/<int:task_id>/")
class TaskDetail(Resource):
    def put(self, task_id):
        try:
            task = TaskService.update_task(task_id, task_ns.payload)
            return task.to_dict()
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, task_id):
        try:
            TaskService.delete_task(task_id)
            return {"message": "Successfully deleted"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {
                "error": "An unexpected error occurred while deleting the task."
            }, 500


@task_ns.route("/<int:task_id>/assign/<int:user_id>")
class TaskAssign(Resource):
    def put(self, task_id, user_id):
        try:
            task = TaskService.assign_task(task_id, user_id)
            return task.to_dict()
        except ValueError as e:
            return {"error": str(e)}, 400
