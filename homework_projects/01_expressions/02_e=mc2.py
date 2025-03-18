speed_of_light = 299792458


def calculate_energy(mass):
    energy = mass * speed_of_light ** 2
    return energy


def main():
    mass = float(input("Enter the mass in Kilograms: "))
    energy = calculate_energy(mass)

    print(
        f"\nIf {mass} kg of mass were converted to energy, it would produce {energy:,.2f} joules.")


if __name__ == "__main__":
    main()
