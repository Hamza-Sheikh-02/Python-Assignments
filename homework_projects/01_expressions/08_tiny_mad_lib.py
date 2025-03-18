SENTENCE_START = "I'm going to the store to buy"


def main():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    sentence = f"{SENTENCE_START} a {adjective} {noun} so I can {verb}."
    print(sentence)


if __name__ == "__main__":
    main()
