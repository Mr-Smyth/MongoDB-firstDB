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

# when adding key value pairs from python, the keys also need quotes.
new_doc = {
    "first": "douglas",
    "last": "adams",
    "dob": "11/03/1952",
    "hair_colour": "grey",
    "occupation": "writer",
    "nationality": "british"
}

coll.insert(new_doc)

documents = coll.find()
# This will return a mongoDB object aka a cursor.
for doc in documents:
    print(doc)
