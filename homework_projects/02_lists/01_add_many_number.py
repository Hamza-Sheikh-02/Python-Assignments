def add_many_number(numbers: list[int]) -> int:
    total = 0

    for number in numbers:
        total += number

    return total


def main():
    numbers: list[int] = [6, 7, 8, 9, 10]

    sum = add_many_number(numbers)
    print(f"The sum of the numbers is {sum}")


if __name__ == "__main__":
    main()
