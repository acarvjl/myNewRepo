# Function to add a contact to the text file
def add_contact_to_file(file_name, contact):
    with open(file_name, "+a") as file:
        file.write(f"{contact['name']}:{contact['phone_number']}:{contact['email_address']}\n")

# Function to display all contacts from the text file
def display_contacts_from_file(file_name):
    with open(file_name, "+r") as file:
        for line in file:
            name, phone_number, email_address = line.strip().split(":")
            print("Name: {name}")
            print("Phone: {phone_number}")
            print("Email: {email_address}")
            print()

# Function to search for contacts in the text file
def search_contacts_in_file(file_name, query):
    found_contacts = []
    with open(file_name, "+r") as file:
        for line in file:
            name, phone_number, email_address = line.strip().split(":")
            if query in name or query in phone_number or query in email_address:
                found_contacts.append({"Name": name, "Phone": phone_number, "Email": email_address})
    return found_contacts

# Main function
def main(): 
    file_name = "contacts.txt"

    while True:
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search contacts")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            contact_info = {}
            contact_info["name"] = input("Enter a contact's name: ")
            contact_info["phone_number"] = input("Enter phone number: ")
            contact_info["email_address"] = input("Enter email address: ")
            add_contact_to_file(file_name, contact_info)
            print("Contact added!")

        elif choice == "2":
            if not open(file_name, "+r").readlines():
                print("No contacts to display.")
            else:
                display_contacts_from_file(file_name)

        elif choice == "3":
            query = input("Enter a name, phone number or email address to search for: ")
            found = search_contacts_in_file(file_name, query)
            if not found:
                print("No matching contacts found.")
            else:
                print("Matching Contacts:")
                for contact in found:
                    print("Contact:", contact)
                    # {contact['name']}:{contact['phone_number']}:{contact['email_address']}
                    print("Name:", contact.get('name'))
                    print("Phone:", contact.get('phone_number'))
                    print("Email:", contact.get('email_address'))
                    print()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select a valid option.")

    print("I'm out of here!")

if __name__ == "__main__":
    main()
