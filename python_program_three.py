# python_program_three.py
#
# Python List and Dictionary Program
# 
# python_program_three 9/12/23
# Python file name: python_program_three.py
# Date: 9/15/2023
# Programmer's name: Adrian Carvajal
# ********************************************************************************************

# Create an empty list called contacts to store contact information. dictionary_name = {key: value} 

contacts = {}
contact = []
# here we add contact info given, to the conatcts dictionary, via the following input lines 

name = input("Enter a contact's name: ")
phone = input("Enter a contact's phone number: ")
email = input("Enter a contact's email address: ")

contacts[name] = {
    'phone': phone,
    'email': email
}
# append a dictionary to a list to retrieve when searching.
contact.append(contacts)

# searching from a dictionary if name in contacts display if not no contacts.
search_name = input("Enter contact name to search for: ")
if search_name not in contacts:
    print("Contact not found")
else:
    print(f"Info matched {name}")
    for index, search_name in enumerate(search_name, start=1):
        if isinstance(contact, dict) and all(key in contact for key in ('name', 'phone_number', 'email_address')):
            print(f"Name: {contact['name']}")
            print(f"Phone Number: {contact['phone']}")
            print(f"Email Address: {contact['email']}")
            print("-" * 30)

# for contacts in contact:
#     for key, value in contacts.items():
#         print(f"{key}: {value}")
#         print("-" * 30)
    
#    print(f"All contacts: {contacts[name]}")
# view contacts, call all by index
print("Contacts:")
for index, contact in enumerate(contacts, start=1):
    if isinstance(contact, dict) and all(key in contact for key in ('name', 'phone_number', 'email_address')):
        print(f"{index}. Name: {contact['name']}")
        print(f"   Phone Number: {contact['phone_number']}")
        print(f"   Email Address: {contact['email_address']}")
        print("-" * 30)
    else:
        print(f"{index}. Invalid contact format:", {contact})
 
    
    
    
# while True:
#     print('1.- Add contact')
#     print('2.- Search contact')
#     print('3.- Exit')
#     choice = input("Enter a choice: ")

#     if choice == '1':
#         add_contacts()
#     elif choice == '2':
#         search_contacts()
#     elif choice == '3':
#         view_contacts()
#     elif choice == '4':
#         break
    
# add_contact()   
# print(contacts)
