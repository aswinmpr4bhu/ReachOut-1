from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

@app.route('/api/getallreqs', methods=['GET'])
def get_all_locations():
  helpreq = mongo.db.helpreqs
  output = []
  for s in helpreq.find():
    output.append(s)
  print(output)
  return str({"data":output})
# @app.route('/api/detail.get/', methods=['GET'])
# def get_one_location(name):
#   location = mongo.db.locations
#   s = location.find_one({'name' : name})
#   if s:
#     output = {'name' : s['name'], 'coord' : s['coord']}
#   else:
#     output = "No such name"
#   return jsonify({'result' : output})

@app.route('/api/posthelpoffer', methods=['POST'])
def add_offer():
  helpoffer = mongo.db.helpoffers
  offer_id = helpoffer.insert(request.json)
  return str(offer_id)

@app.route('/api/posthelp', methods=['POST'])
def add_req():
  helpreq = mongo.db.helpreqs
  req_id = helpreq.insert(request.json)
  return str(req_id)

if __name__ == '__main__':
    app.run(debug=True)
    print("server running....")