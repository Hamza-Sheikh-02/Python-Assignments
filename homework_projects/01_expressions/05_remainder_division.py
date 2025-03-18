def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    quotient = num1 // num2
    remainder = num1 % num2

    print(
        f"\nWhen {num1} is divided by {num2}, the quotient is {quotient} and the remainder is {remainder}.")


if __name__ == "__main__":
    main()
