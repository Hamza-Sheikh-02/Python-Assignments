def square_number(number: float) -> float:
    result = number ** 2
    return result


def main():
    number = float(input("Enter a number: "))
    squared = square_number(number)
    print(f"\nThe square of {number} is {squared:.2f}")


if __name__ == "__main__":
    main()
