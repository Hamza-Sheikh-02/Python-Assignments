def get_first_element(lst):
    return lst[0]


def get_lst():
    lst = []
    element = input("Enter an element of the list: ")
    while element != "":
        lst.append(element)
        element = input(
            "Enter an element of the list (or press Enter to end): ")
    return lst


def main():
    lst = get_lst()
    first_element = get_first_element(lst)
    print(f"\nThe first element is: {first_element}")


if __name__ == "__main__":
    main()
