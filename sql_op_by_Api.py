# ...........CURD OPERATION ON SQL BY USING API.............

from flask import Flask , request , jsonify
from mysql import connector as myconnector
app = Flask(__name__)
# connection established

config = {'user':'root','password':'Jigar@975919','host':'localhost','database':'taskdb'}

try:
    conne = myconnector.connect(**config)
    if conne.is_connected():
        print('connected')
except:
    print('unable to connect')
myc = conne.cursor()
myc.execute("create database if not exists taskdb")
myc.execute("create table if not exists taskdb.tasktable (name varchar(30),number int)")

@app.route('/insert', methods=['POST'])
def insert():
    if (request.method=="POST"):
        name = request.json['name']
        number = request.json['number']
        param = (name , number)
        query = "insert into taskdb.tasktable (name , number) values(%s , %s)"
        myc.execute(query , param)
        conne.commit()
        return jsonify(str('succesfully inserted'))


@app.route('/update', methods=['POST'])
def update():
    if (request.method=="POST"):
        name = request.json['name']
        number = request.json['number']
        query = "UPDATE taskdb.tasktable SET name = %s WHERE number = %s"
        param = (name , number)
        myc.execute(query , param)
        conne.commit()
        return jsonify(str('succesfully updated'))

@app.route('/fetch', methods=['POST'])
def fecth():
    if (request.method=="POST"):
        
        number = request.json['number']
        query = "SELECT * FROM taskdb.tasktable WHERE number = %s"
        param = ( number,)      # scaler value tuple
        myc.execute(query , param)
        row = myc.fetchall()
        for item in row:
            return jsonify(str(item))
        return jsonify(str('succesfully fetched'))

if __name__ == "__main__":
    app.run(port=5005)   # keep change the port no. if you are getting error
