from hashlib import sha256


def hash_password(password):
    return sha256(password.encode()).hexdigest()


def login(email, stored_logins, password_to_check):
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True
    return False


def main():
    stored_logins = {
        "demo@login.com": hash_password("DemoPass123"),
    }

    print(login("demo@login.com", stored_logins, "wrongpass"))
    print(login("demo@login.com", stored_logins, "DemoPass123"))


if __name__ == "__main__":
    main()
