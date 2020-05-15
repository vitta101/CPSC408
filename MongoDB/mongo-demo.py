# pip install pymongo
# pip install dnspython
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://root:K2AkdYas8lsNGO7o@cluster0-lokzt.gcp.mongodb.net/cpsc408-mongo-test?retryWrites=true&ssl_cert_reqs=CERT_NONE")
print(myclient.list_database_names())

db = myclient['cpsc408-mongo-test']

#select document
for s in db.Student.find():
    print(s)

#select document with criteria
# for s in db.Student.find({"major":{"Seq":"COMM"}}):
#     print(s)
for s in db.Student.find({"major":"COMM"}):
    print(s)

#insert new document
db.Student.insert_one({"FirstName":"Ananya","LastName":"Vittal","major":["Data Analytics","BUS"],"Courses":["CPSC 350","CPSC 408","ECON 452"]})
