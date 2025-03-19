MAX_TERM_VALUE: int = 10000


def main() -> None:
    current_term: int = 0
    next_term: int = 1

    while current_term < MAX_TERM_VALUE:
        print(current_term, end=" ")
        current_term, next_term = next_term, current_term + next_term


if __name__ == "__main__":
    main()
