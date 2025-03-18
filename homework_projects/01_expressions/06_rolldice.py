import random


def main():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"\nTotal: {total}")


if __name__ == "__main__":
    main()
