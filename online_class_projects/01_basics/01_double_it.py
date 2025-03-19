def main() -> None:
    user_number: int = int(input("Enter a number: "))

    while user_number < 100:
        print(user_number * 2, end=" ")
        user_number *= 2


if __name__ == "__main__":
    main()
