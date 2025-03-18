import math


def main():
    opposite = float(input("Enter the length of the opposite side: "))
    adjacent = float(input("Enter the length of the adjacent side: "))

    hypotenuse = math.sqrt(opposite**2 + adjacent**2)
    print(f"\nThe length of the hypotenuse is {hypotenuse:.2f}.")


if __name__ == "__main__":
    main()
