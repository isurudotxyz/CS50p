import random


def main():
    level = get_level()
    random_number = random.randint(1, level)
    guess(random_number)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise TypeError
        except:
            pass
        else:
            return n
            break


def guess(n):
    # prompt user to guess the random number
    #  if random number right print just right and exit
    # if random number is lower print Too small!
    # if random number is to high print Too large! and prompt again
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise TypeError
        except:
            pass
        else:
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            elif guess == n:
                print("Just right!")
                break


if __name__ == "__main__":
    main()
