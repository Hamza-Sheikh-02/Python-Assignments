def get_phonebook_entries():
    phonebook = {}

    while True:
        name = input("Enter a name: ").lower()
        if name == "":
            break
        phone = input("Enter a phone number: ")
        phonebook[name] = phone

    return phonebook


def display_phonebook(phonebook):
    print("\nPhonebook:")
    print("----------")
    for name, phone in phonebook.items():
        print(f"\n{name}: {phone}")


def search_phonebook(phonebook):
    while True:
        name = input("Enter a name: ").lower()
        if name == "":
            break
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Not found")


def main():
    phonebook = get_phonebook_entries()
    display_phonebook(phonebook)
    search_phonebook(phonebook)


if __name__ == "__main__":
    main()
