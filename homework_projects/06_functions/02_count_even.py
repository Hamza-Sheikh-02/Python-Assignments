def count_even(lst: list[int]) -> int:
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


def get_list() -> list[int]:
    lst = []
    while True:
        user_input = input("Enter a number or press enter to finish: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return lst


def main():
    lst = get_list()
    print(f"\nThe number of even numbers is {count_even(lst)}")


if __name__ == "__main__":
    main()
