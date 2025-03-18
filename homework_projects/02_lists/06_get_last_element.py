def get_last_element(lst):
    return lst[-1]


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
    last_element = get_last_element(lst)
    print(f"\nThe last element is: {last_element}")


if __name__ == "__main__":
    main()
