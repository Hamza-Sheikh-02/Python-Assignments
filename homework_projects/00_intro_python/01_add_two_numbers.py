def add_numbers(num1: int, num2: int) -> int:
    result = num1 + num2
    return result


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = add_numbers(num1, num2)

    print(f"\nThe sum of {num1} and {num2} is {result}")


if __name__ == "__main__":
    main()
