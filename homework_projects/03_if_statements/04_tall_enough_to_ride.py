def main():
    MIN_HEIGHT = 50

    while True:
        height_input = input("How tall are you? ")

        if height_input == "":
            break

        try:
            height = int(height_input)
        except ValueError:
            print("\nPlease enter a valid number.\n")
            continue

        if height >= MIN_HEIGHT:
            print(f"\nYou're tall enough to ride!\n")
        else:
            print(
                f"\nYou're not tall enough to ride, but maybe next year!\n")


if __name__ == "__main__":
    main()
