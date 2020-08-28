import os
from os import system, name
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
    print("5. Clear the screen")
    print("6. Exit")

    option = input("Enter an option: ")
    return option


def get_record():

    # This is a helper function to assist in the searches
    # That will need to be done in finding, editing and deleting
    # Records

    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    first = first.strip(" ")
    last = last.strip(" ")

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


def find_record():

    # Fuction to find and display a users record

    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())


def edit_record():

    # Function that gets the required record then
    # Then iterates over it, giving the user an 
    # option to change any particular field

    doc = get_record()
    if doc:
        # create update_doc, we will add values to this dictionary
        # While iterating over the key value pairs of the selected
        # Record
        update_doc = {}
        print("")
        # for each key,value pair
        for key, value in doc.items():
            # check iteration is not on the secret id
            if key != "_id":
                # Then display the current key and value,
                # and allow user to change value
                update_doc[key] = input(
                    key.capitalize(
                    ) + " [" + value + "] (press enter to skip..) >")

                # set input to lowercase and strip any unwanted whitespace
                update_doc[key] = update_doc[key].lower()
                update_doc[key] = update_doc[key].strip(" ")

                # If field has not changed, set the key to the original value
                if update_doc[key] == "":
                    update_doc[key] = value

        # try and insert into Mongo DB and handle any error
        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated successfully!")
        except:
            print("Error accessing the database")


def del_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())

        print("")
        confirmation = input("Are you sure this is the record you want to delete?\nY/N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("*"*50)
                print("The requested document has been deleted")
                print("*"*50)
            except:
                print("There was an error accessing the database, please try again.")
        else:
            print("The document was NOT deleted")


def clear(): 
  
    # Function to clear the screen

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def main_loop():

    # MAIN LOOP-
    # HANDLES CALLING OF MENU
    # HANDLES RESPONSE TO OPTION SELECTION

    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            del_record()
        elif option == "5":
            clear()
        elif option == "6":
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
