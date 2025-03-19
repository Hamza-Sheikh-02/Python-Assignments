import random


def main():
    print("I am thinking of a number between 1 and 99")
    secret_number = random.randint(1, 99)

    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess == secret_number:
            print("\nYou guessed the number!")
            break
        elif user_guess < secret_number:
            print("\nToo low!")
        elif user_guess > secret_number:
            print("\nToo high!")
        else:
            print("\nInvalid input!")


if __name__ == "__main__":
    main()
