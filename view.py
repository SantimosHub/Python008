def print_contacts(contacts: dict):
    for count, key in enumerate(sorted(contacts)):
        print(f"{count + 1}\t{key}\t{contacts[key]}")
    print()


def print_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))


def input_data(message: str):
    data = input(message)
    return data
