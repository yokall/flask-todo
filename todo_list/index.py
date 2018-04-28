from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {'description': 'Clean car', 'done': False}
]


@app.route('/todos')
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    todos.append(request.get_json())
    return '', 204
