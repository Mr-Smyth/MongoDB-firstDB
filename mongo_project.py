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
        return conn
    except pymongo.errors.connectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():

    # CREATE OUR MENU  WITH INPUT PROMPT

    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter an option: ")
    return option


def get_record():

    # This is a helper function to assist in the searches
    # That will need to be done in finding, editing and deleting
    # Records

    print("")
    first = input("Enter first name > ")
    last = input("Enter last name")

    # try to search for name and handle any errors
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("An error has occured accessing the database")

    # if no documents are found
    if not doc:
        print("")
        print("Sorry, but no documents matching your criteria were found")

    return doc


def add_record():

    # This functions handles option 1. Add a record.
    # It collects the data from the user
    # it creates a dictionary of the key: value pairs
    # It inserts to Mongo DB

    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter their date of birth > ")
    gender = input("Enter their gender > ")
    hair_colour = input("Enter their hair colour > ")
    occupation = input("Enter their occupation > ")
    nationality = input("Enter their nationality > ")

    # Insert the inputs into a dictionary, to prep for insertion.
    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob.lower(),
        "gender": gender.lower(),
        "hair_colour": hair_colour.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower()
    }

    # try to insert the data and handle errors
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("An error has occured accessing the database")


def main_loop():

    # MAIN LOOP-
    # HANDLES CALLING OF MENU
    # HANDLES RESPONSE TO OPTION SELECTION

    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("That is an invalid option")
        print("")


# CALL OUR MONGO CONNECTION
# CREATE OUR MONGO CELEBRITIES COLLECTION

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# CALL THE MAIN LOOP

main_loop()
