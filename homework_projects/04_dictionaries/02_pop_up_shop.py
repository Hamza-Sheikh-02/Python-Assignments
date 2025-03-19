def main() -> None:
    fruits: dict[str, float] = {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 0.75,
        "pear": 1.25,
        "pineapple": 2.0,
    }

    total_cost: float = 0.0

    for fruit, price in fruits.items():
        quantity: int = int(
            input(f"How many {fruit}s would you like to buy? "))
        total_cost += price * quantity

    print(f"\nThe total cost of your purchase is ${total_cost:.2f}")


if __name__ == "__main__":
    main()
