AFFIRMATION_TEXT: str = "I believe in my ability to overcome any challenge."


def main() -> None:
    user_response: str = input(
        f"Please type the following affirmation exactly as shown:\n{AFFIRMATION_TEXT}\n\n"
    ).lower()

    while user_response != AFFIRMATION_TEXT.lower():
        print("That doesn't match the affirmation.")
        print(
            f"\nTry again. Type the following affirmation exactly:\n{AFFIRMATION_TEXT}\n\n"
        )
        user_response = input().lower()

    print("Correct! Your positive mindset is inspiring!")


if __name__ == "__main__":
    main()
