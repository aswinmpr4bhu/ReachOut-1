from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)


location = 
requirements =

@app.route('/api/location.get', methods=['GET'])
def get_tasks():
    return jsonify({'location':location})

@app.route('/api/requirements.get', methods=['GET'])
def get_tasks():
    return jsonify({'requirements':requirements})

@app.route('/api/details.post', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        '': tasks[-1]['id'] + 1,
        '': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)