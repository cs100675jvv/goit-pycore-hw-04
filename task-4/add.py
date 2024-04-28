def add_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return print(f"Contact {name} with {phone} added.")
    else:
        return print(f"Contact {name} with phone {contacts[name]} already exist.")