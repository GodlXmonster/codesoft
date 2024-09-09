import json

# Load contacts from a JSON file
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to a JSON file
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"Contact {index + 1}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}")
            print()

# Search for a contact
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

# Update a contact
def update_contact(contacts):
    search_term = input("Enter the name or phone number of the contact to update: ")
    contact = next((c for c in contacts if search_term in c['name'] or search_term in c['phone']), None)
    
    if contact:
        print("Leave the field blank if you do not want to update it.")
        name = input(f"New name ({contact['name']}): ") or contact['name']
        phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
        email = input(f"New email ({contact['email']}): ") or contact['email']
        address = input(f"New address ({contact['address']}): ") or contact['address']
        
        contact.update({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
