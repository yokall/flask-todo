from flask import Flask, jsonify, request

from todo_list.model.todo import ToDo, ToDoSchema

app = Flask(__name__)

tasks = [
    ToDo("Wash car", False),
    ToDo("Tidy room", False),
    ToDo("Get groceries", True),
]


@app.route('/todos')
def get_todos():
    schema = ToDoSchema(many=True)
    todos = schema.dump(
        tasks
    )
    return jsonify(todos.data)


@app.route('/todos', methods=['POST'])
def add_todo():
    todo = ToDoSchema().load(request.get_json())
    tasks.append(todo.data)
    return '', 204


if __name__ == "__main__":
    app.run()
