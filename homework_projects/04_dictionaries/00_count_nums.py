def get_numbers():
    numbers_list = []

    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        numbers_list.append(int(number))

    return numbers_list


def count_numbers(numbers_list):
    number_dict = {}

    for number in numbers_list:
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1

    return number_dict


def print_count(number_dict):
    for number, count in number_dict.items():
        print(f"The number {number} was appeared {count} times.")


def main():
    numbers_list = get_numbers()
    number_dict = count_numbers(numbers_list)
    print_count(number_dict)


if __name__ == "__main__":
    main()
