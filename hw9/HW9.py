def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please enter a valid command."
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid input. Please try again."
    return inner


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def get_phone(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        raise KeyError


def show_all_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():
    while True:
        user_input = input("Enter a command: ").lower()
        
        if user_input == "hello":
            print("How can I help you?")
        
        elif user_input.startswith("add"):
            try:
                _, name, phone = user_input.split()
                result = add_contact(name, phone)
                print(result)
            except ValueError:
                print("Please enter name and phone number separated by a space.")
        
        elif user_input.startswith("change"):
            try:
                _, name, phone = user_input.split()
                result = change_contact(name, phone)
                print(result)
            except ValueError:
                print("Please enter name and phone number separated by a space.")
        
        elif user_input.startswith("phone"):
            try:
                _, name = user_input.split()
                result = get_phone(name)
                print(result)
            except ValueError:
                print("Please enter a name.")
        
        elif user_input == "show all":
            show_all_contacts()
        
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
