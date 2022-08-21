# >......insert data into mongodb atlas by using Api..........

from flask import Flask, request,jsonify
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://Ranjit_singh:<password>@learning.a5xc4jg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
@app.route('/insertmg',methods = ['GET','POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name'] 
        age = request.json['age'] 
        roll = request.json['roll'] 
        city = request.json['city'] 
        json_record = {"name":name,"age":age,"roll":roll,"city":city}
        path_of_collection = client.database1.collection1
        path_of_collection.insert_one(json_record)
        return jsonify(str('succesfully inserted'))

if __name__ == "__main__":
    app.run(port=5005)

