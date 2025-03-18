def main():
    numbers: list[int] = [6, 7, 8, 9, 10]

    for i in range(len(numbers)):
        numbers[i] *= 2

    print(numbers)


if __name__ == "__main__":
    main()
