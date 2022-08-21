...........inserted data into mongodb atlas...........
import pymongo 
client = pymongo.MongoClient("mongodb+srv://Ranjit_singh:<password>@learning.a5xc4jg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db1 = client['database1']
coll = db1['collection1']

json_record = { "name":"durge","age":100,"roll":1,"city":"paradis"}
coll.insert_one(json_record)
print('successfully inserted your data')
