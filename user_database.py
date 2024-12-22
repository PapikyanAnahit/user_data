import json
import os

my_file = "name.json"

def load_database():
    try:
        with open(my_file, "r") as file:
            data = json.load(file) or []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

def save_database(data):
    with open(my_file, "w") as file:
        json.dump(data, file)

def user_add():
    name = input("Input name: ")
    age = input("Input age: ")
    user = {"name": name, "age": age}
    data = load_database()
    data.append(user)
    save_database(data)
    print(f"User {name} added!")


def user_view():
    data = load_database()
    if not data:
        print("No users in the database.")
    else:
        print("User Records:")
        for user in data:
            print(user['name'] + ", " + user['age'])

def user_delete():
    name_to_remove = input("Enter the name of the user to delete: ")
    data = load_database()
    found = False
    for user in data:
        if user['name'] == name_to_remove:
            data.remove(user)
            save_database(data)
            print(f"User {name_to_remove} deleted.")
            found = True
            break
    if not found:
        print(f"No user named {name_to_remove} found.")

def exit_program():
    print("Goodbye!")
    exit()

while True:
    print("Options:")
    print("1. Add a User")
    print("2. View Users")
    print("3. Delete User")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        user_add()
    elif choice == "2":
        user_view()
    elif choice == "3":
        user_delete()
    elif choice == "4":
        exit_program()
    else:
        print("Invalid option.")
