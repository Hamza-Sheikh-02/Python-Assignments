import random


def guess_the_number(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {number}: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
        elif guess == random_number:
            print("You guessed the number!")
            break
    return guess


def main():
    guess_the_number(10)


if __name__ == "__main__":
    main()
