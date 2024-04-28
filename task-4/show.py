def show_phone (args, contacts):
    name, = args
    if name in contacts:
        return print(f"Contact {name} has phone: {contacts[name]}")
    else:
        return print(f"Contact {name} not found in our dictionary.")


def show_all (contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")