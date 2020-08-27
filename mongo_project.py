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


def main_loop():

    # MAIN LOOP-
    # HANDLES CALLING OF MENU
    # HANDLES RESPONSE TO OPTION SELECTION

    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
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
