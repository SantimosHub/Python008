import view
import service

file_name = "contacts.txt"


def start():
    view.print_message("Phonebook is open")
    while True:
        action = int(view.input_data(
            "Enter the number of action:\n1 — Show\n2 — Find\n3 — Add\n4 — Edit\n5 - Delete\n0 — Exit\n>>> "))
        if action == 0:
            view.print_message('Phonebook is closed')
            break
        elif action == 1:
            view.print_contacts(service.load_data(file_name))
        elif action == 2:
            text = view.input_data("Enter what to find: ")
            find_result = service.find_contacts(service.load_data(file_name), text)
            view.print_contacts(find_result)
        elif action == 3:
            name = view.input_data("Enter the name: ")
            number = view.input_data("Enter the number: ")
            service.add_data(file_name, name, number)
            view.print_message('Contact is added')
        elif action == 4:
            text = view.input_data("Enter what to edit: ")
            new_text = view.input_data("Enter new value: ")
            service.edit_data(file_name, service.load_data(file_name), text, new_text)
            view.print_message('Contact is edit')
        elif action == 5:
            text = view.input_data("Enter what to delete: ")
            service.delete_data(file_name, service.load_data(file_name), text)
            view.print_message('Contact is delete')
        else:
            view.print_message("The number is incorrect.")
