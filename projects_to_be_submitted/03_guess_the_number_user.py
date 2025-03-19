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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly!")


def main():
    computer_guess(10)


if __name__ == "__main__":
    main()
