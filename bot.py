def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return "Contact was not found."

    contacts[name] = phone

    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]

    if name not in contacts:
        return "Contact was not found."

    return contacts[name]


def show_all(contacts):
    prepared_data = []

    for name in contacts:
        prepared_data.append(f"{name}: {contacts[name]}")

    return "\n".join(prepared_data)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception:
            print("Invalid arguments for command:", command)


if __name__ == "__main__":
    main()
