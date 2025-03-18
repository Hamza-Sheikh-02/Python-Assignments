MAX_LENGTH = 3


def shorten(lst):
    while len(lst) > MAX_LENGTH:
        lst.pop()
    return lst


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
    shortened_lst = shorten(lst)
    print(f"\nThe shortened list is: {shortened_lst}")


if __name__ == "__main__":
    main()
