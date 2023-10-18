def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    conversion = gauge(percentage)
    print(conversion)


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(y) < int(x):
        raise ValueError
    else:
        x = int(x)
        y = int(y)
        percentage = round(((x / y) * 100))
        return percentage


def gauge(percentage):
    try:
        if percentage >= 99:
            return "F"
        elif 0 <= percentage <= 1:
            return "E"
        elif 1 < percentage < 99:
            return f"{percentage}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()
