from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/api/detail.get', methods=['GET'])
def get_all_locations():
  location = mongo.db.locations
  output = []
  for s in location.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/api/detail.get/', methods=['GET'])
def get_one_location(name):
  location = mongo.db.locations
  s = location.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/api/detail.post', methods=['POST'])
def add_location():
  location = mongo.db.locations
  name = request.json['name']
  distance = request.json['distance']
  location_id = location.insert({'name': name, 'distance': distance})
  new_location = location.find_one({'_id': location_id })
  output = {'name' : new_location['name'], 'distance' : new_location['distance']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)