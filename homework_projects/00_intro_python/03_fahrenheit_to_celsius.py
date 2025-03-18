def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius


def main():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"\n{fahrenheit} degrees fahrenheit is {celsius:.2f} degrees celsius.")


if __name__ == "__main__":
    main()
