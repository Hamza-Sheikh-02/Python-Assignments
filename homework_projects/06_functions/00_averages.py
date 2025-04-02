def average(num1: float, num2: float) -> float:
    sum = num1 + num2
    average = sum / 2
    return average


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"\nThe average of {num1} and {num2} is {average(num1, num2)}")


if __name__ == "__main__":
    main()
