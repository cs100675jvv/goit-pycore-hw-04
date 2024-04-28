def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return print(f"Contact {name} now has phone: {contacts[name]}")
    else:
        return print(f"Contact {name} not found in our dictionary.")