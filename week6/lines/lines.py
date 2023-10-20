import sys


# count lines from a python
# exclude blank lines or comment
#
def main():
    # too few cml
    # too many cml
    # not a python file
    # file does not exist
    n = len(sys.argv)
    try:
        if n > 2:
            sys.exit("Too many command-line arguments")
        elif n < 2:
            sys.exit("Too few command-line arguments")
        elif sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            counter = 0
            path = sys.argv[1]
            # path = f"/Users/999isuru/repos/cs50p/week6/lines/{sys.argv[1]}"
            with open(path, "r") as file:
                for line in file:
                    if not (line.lstrip().startswith("#") or line.strip() == ""):
                        counter = counter + 1

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(counter)


if __name__ == "__main__":
    main()
