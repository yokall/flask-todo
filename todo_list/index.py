import os
import logging

from flask import Flask, jsonify, request
from pymongo import MongoClient

from todo_list.model.todo import ToDo, ToDoSchema

app = Flask(__name__)

if app.config['ENV'] == "development":
    config = os.path.join(app.root_path, 'config/development.cfg')
else:
    config = os.path.join(app.root_path, 'config/production.cfg')

app.config.from_pyfile(config)

client = MongoClient(app.config['MONGO_URL'])
db = client['flask_todo']


@app.route('/todos')
def get_todos():
    tasks = db.tasks.find()

    schema = ToDoSchema(many=True)
    todos = schema.dump(
        tasks
    )

    return jsonify(todos.data)


@app.route('/todos', methods=['POST'])
def add_todo():
    todo = ToDoSchema().load(request.get_json())
    db.tasks.insert_one(todo.data)
    return '', 204


if __name__ == "__main__":
    app.run()
