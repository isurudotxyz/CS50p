# inset the input in fraction x/y
# if value error prompt again
# if value of y is 0 or greater than x ask to prompt again
# print the converted percentage
while True:
    try:
        fraction = input("Fraction: ")
        x, y = (fraction).split("/")
        x = int(x)
        y = int(y)

        if y != 0 and y >= x:
            percentage = round(((x / y) * 100))
            break

    except ValueError:
        pass

    except ZeroDivisionError:
        pass

if percentage >= 99:
    print("F", end="")
elif 0 <= percentage <= 1:
    print("E", end="")
else:
    print(f"{percentage}%", end="")
