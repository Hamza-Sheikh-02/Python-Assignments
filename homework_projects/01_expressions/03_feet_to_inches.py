inches_per_foot = 12


def convert_to_inches(feet: float) -> float:
    inches = feet * inches_per_foot
    return inches


def main():
    feet = float(input("Enter the number of feet: "))
    inches = convert_to_inches(feet)
    print(f"{feet:.2f} feet is equal to {inches:.2f} inches.")


if __name__ == "__main__":
    main()
