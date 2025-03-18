def get_list():
    lst = []
    element = input("Enter an element of the list: ")
    while element != "":
        lst.append(element)
        element = input(
            "Enter an element of the list (or press Enter to end): ")
    return lst


def main():
    lst = get_list()
    print(f"\nThe list is: {lst}")


if __name__ == "__main__":
    main()
