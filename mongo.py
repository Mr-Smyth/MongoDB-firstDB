import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.connectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# Update multiple records:
coll.update_many({"nationality": "american"}, {"$set": {"hair_colour": "maroon"}})


documents = coll.find({"nationality": "american"})
# This will return a mongoDB object aka a cursor.
for doc in documents:
    print(doc)
