import random

DONE_LIKELIHOOD = 0.1


def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=' ')


def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():
    chaotic_counting()
    print("\nDone")


if __name__ == "__main__":
    main()
