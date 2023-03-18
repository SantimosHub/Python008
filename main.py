
import service as s

file_name = "contacts.txt"

print("Phonebook is open")
while True:
    action = int(input(
        "Enter the number of action:\n1 — Show\n2 — Find\n3 — Add\n4 — Edit\n5 - Delete\n0 — Exit\n>>> "))
    if action == 0:
        print('Phonebook is closed')
        break
    elif action == 1:
        s.print_contacts(s.load_data(file_name))
        print()
    elif action == 2:
        text = input("Enter what to find: ")
        s.find_contacts(s.load_data(file_name), text)
        print()
    elif action == 3:
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        s.add_data(file_name, name, number)
        print()
    elif action == 4:
        text = input("Enter what to edit: ")
        new_text = input("Enter new value: ")
        s.edit_data(file_name, s.load_data(file_name), text, new_text)
        print()
    elif action == 5:
        text = input("Enter what to delete: ")
        s.delete_data(file_name, s.load_data(file_name), text)
        print()
    else:
        print("The number is incorrect.")
