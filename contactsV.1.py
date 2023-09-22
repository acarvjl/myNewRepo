# creating a fuction to open a file to add contacts.
# while this creates a file as well, I will be updating
while True:
    choice = input('Add (1) Search (2) Quit (3) ')
    if choice == '1':
        with open("contacts.txt", "a") as file:
            name = input('Name: ')
            phone_number = input("Phone: ")
            email_address = input("Email: ")
            file.writelines((name, ' : ', phone_number, ' : ', email_address, '\n'))
    elif choice == '2':
        with open("contacts.txt", "r") as file:
            search = input("Search contacts file: ")
            for i in file:
                if search in i:
                    print(i)
    else:
        break
