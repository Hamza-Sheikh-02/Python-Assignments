import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")


def main():
    t = int(input("Enter the time in seconds: "))
    countdown(t)


if __name__ == '__main__':
    main()
