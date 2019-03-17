from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("127.0.0.1", 27017)
# conn = MongoClient("mongodb://{user}:password@127.0.0.1:27017")
db = conn.kaze
collection = db.logstash_test
# collection.find_one()
for record in collection.find({'_id': ObjectId('5c661458fadb9213373e879b')}):
    print(record)
