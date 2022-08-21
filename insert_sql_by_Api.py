# ............insert data into sql by using Api.............


from flask import Flask , request , jsonify
from mysql import connector as myconnector
app = Flask(__name__)
config = {'user':'root','password':'Jigar@975919','host':'localhost','database':'ineuron'}

try:
    conne = myconnector.connect(**config)
    if conne.is_connected():
        print('connected')
except:
    print('unable to connect')


@app.route('/insert',methods = ['GET','POST'])
def insertfunction():            # must be a function in Api
    if (request.method == 'POST'):
        id = request.json['id']

        names = request.json['name']
        roll_no = request.json['roll']
        ag = request.json['age']
        cities =request.json['city']
        myc = conne.cursor()  # cursor object
        query = 'insert into ineuronstudent (stuid,name,roll,age,city) values(%s, %s, %s , %s ,  %s )'
        data = (  id ,names, roll_no, ag, cities)
        
        
        try:
            myc.execute(query,data)
            conne.commit()
            # print(myc.rowcount, 'Row inserted')
        except:
            # print('unable to insert !')
            conne.rollback()
        myc.close()
        conne.close()

if __name__ == "__main__":
    app.run()

