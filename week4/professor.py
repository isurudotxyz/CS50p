import random
import inflect

p = inflect.engine


def main():
    l = get_level()

    # expression
    counter = 0

    for i in range(10):
        x, y = generate_integer(l)
        result = x + y
        while True:
            for i in range(3):
                user = input(f"{x} + {y} = ")
                user_result = int(user)
                if user_result != result:
                    print("EEE")
                elif user_result == result:
                    counter += 1
                    break
                if i == 2:
                    print(f"{x} + {y} = {result}")
            break
    print(f"Score: {counter}")


def get_level():
    # prompt user for level between 1 2 or 3
    while True:
        try:
            prompt = input("Level: ")
            n = int(prompt)
            if n <= 0 or n > 3:
                raise ValueError
        except (TypeError, KeyError, ValueError):
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()
