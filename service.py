def load_data(file_name: str) -> dict:
    contacts = {}
    with open(file_name, "r", encoding='UTF-8') as file:
        for el in file.read().split("\n"):
            contact = el.split(", ")
            if contact != [""]:
                contacts[contact[0]] = contact[1]
    return contacts


def find_contacts(contacts: dict, text: str):
    result = {}
    for key in sorted(contacts):
        if key.lower().__contains__(text.lower()) \
                or contacts[key].replace(" ", "").replace("-", "").__contains__(text.replace(" ", "").replace("-", "")):
            result[key] = contacts[key]
    return result


def add_data(file_name: str, name: str, number: str):
    with open(file_name, "a") as file:
        file.writelines(f"{name}, {number}\n")


def edit_data(file_name: str, contacts: dict, text: str, new_text: str):
    for key in sorted(contacts):
        if key.lower().__contains__(text.lower()):
            contacts[new_text] = contacts.pop(key)
        elif contacts[key].replace(" ", "").replace("-", "").__contains__(text.replace(" ", "").replace("-", "")):
            contacts[key] = new_text
    save_file(file_name, contacts)


def delete_data(file_name: str, contacts: dict, text: str):
    for key in sorted(contacts):
        if key.lower().__contains__(text.lower()) \
                or contacts[key].replace(" ", "").replace("-", "").__contains__(text.replace(" ", "").replace("-", "")):
            del contacts[key]
    save_file(file_name, contacts)


def save_file(file_name: str, contacts: dict):
    with open(file_name, "w", encoding='UTF-8') as file:
        for key in sorted(contacts):
            file.writelines(f"{key}, {contacts[key]}\n")
