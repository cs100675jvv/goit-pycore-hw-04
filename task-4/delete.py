def delete_contact(args, contacts):
    name, = args
    del contacts[name]
    return print(f"Contact {name} deleted.")