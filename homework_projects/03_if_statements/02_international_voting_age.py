PETURKSBOUIPO_VOTING_AGE: int = 16
STANLAU_VOTING_AGE: int = 25
MAYENGUA_VOTING_AGE: int = 48


def main():
    user_country = input(
        "What is your country (Peturksbouipo, Stanlau, Mayengua)? ").title()
    user_age = int(input("How old are you? "))

    if user_country == "Peturksbouipo":
        if user_age >= PETURKSBOUIPO_VOTING_AGE:
            print(
                f"\nYou can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}")
        else:
            print(
                f"\nYou cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}")

    if user_country == "Stanlau":
        if user_age >= STANLAU_VOTING_AGE:
            print(
                f"\nYou can vote in Stanlau where the voting age is {STANLAU_VOTING_AGE}")
        else:
            print(
                f"\nYou cannot vote in Stanlau where the voting age is {STANLAU_VOTING_AGE}")

    if user_country == "Mayengua":
        if user_age >= MAYENGUA_VOTING_AGE:
            print(
                f"\nYou can vote in Mayengua where the voting age is {MAYENGUA_VOTING_AGE}")
        else:
            print(
                f"\nYou cannot vote in Mayengua where the voting age is {MAYENGUA_VOTING_AGE}")


if __name__ == "__main__":
    main()
