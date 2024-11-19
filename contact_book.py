contacts={"name": "", "phone":"", "email":"" ,"address":""}

def add_contact():
    name = input("Enter name: ")
    contacts["name"]=name
    phone = int(input("Enter phone number: "))
    contacts["phone"]=phone
    email = input("Enter email: ")
    contacts["email"]=email
    address = input("Enter address: ")
    contacts["address"]=address
    if name in contacts:
        print("\nContact with this name already exists.")
        print("\nContact added successfully.")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        print("NAME : ",contacts["name"])
        print("PHONE : ",contacts["phone"])
        print("EMAIL : ",contacts["email"])
        print("ADDRESS : ",contacts["address"])

def search_contact():
    query = input("\nEnter name to search: ")
    found = False
    if query in contacts["name"]:
        print("Contact Found")
        print("")
        print("NAME : ",contacts["name"])
        print("PHONE : ",contacts["phone"])
        print("EMAIL : ",contacts["email"])
        print("ADDRESS : ",contacts["address"])
        found = True
        if not found:
            print("\nNo contact found.")


def update_contact():
    name = input("\nEnter the name of the contact to update: ").strip()
    if name in contacts:
        print("\nEnter new details (leave blank to keep current value):")
        phone = input("New phone number: ")
        contacts["phone"]=phone
        email = input("New email: ")
        contacts["email"]=email
        address = input("New address: ")
        contacts["address"]=address
        print("\nContact updated successfully.")
    else:
        print("\nContact not found.")


def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    verify = input("Do you want to delete the contact (y/n): ")
    if verify == "y":
        if name in contacts:
            del contacts["name","phone","email","address"]
            print("\nContact deleted successfully.")
        else:
            print("\nContact not found.")
true_or_false =True
while true_or_false:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nChoose an option: ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("\nExiting Contact Manager. Goodbye!")
        true_or_false = False
    else:
        print("\nInvalid option. Please try again.")