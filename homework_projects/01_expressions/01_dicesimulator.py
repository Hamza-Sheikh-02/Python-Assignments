import random


def roll_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    return die_1, die_2


def main():
    for i in range(3):
        print(f"Roll {i+1}:")
        die_1, die_2 = roll_dice()
        print(f"Die 1: {die_1}")
        print(f"Die 2: {die_2}")

        print()


if __name__ == "__main__":
    main()
