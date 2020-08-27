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

"""

To find someone in the database with the first name of “douglas”:
•	documents = coll.find({"first": "douglas"})

To remove someone from the database with the first name of “douglas”:
•	coll.remove({"first": "douglas"})

To update one record in the database:
•	coll.update_one({"nationality": "american"},
                    {"$set": {"hair_colour": "maroon"}})
•	This above code will update the first record it
    reads with the nationality of american.

To update multiple records in a database:
•	coll.update_many({"nationality": "american"},
                    {"$set": {"hair_colour": "maroon"}})
•	The update_many, will update any record it
    reads with the nationality of americn.

"""

# Update multiple records:
coll.update_many({"nationality": "american"}, {"$set": {"hair_colour": "maroon"}})


documents = coll.find({"nationality": "american"})
# This will return a mongoDB object aka a cursor.
for doc in documents:
    print(doc)
