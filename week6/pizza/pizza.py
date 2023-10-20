import sys
import csv
from tabulate import tabulate

n = len(sys.argv)
rows = []


def main():
    try:
        if n > 2:
            sys.exit("Too few command-line arguments")
        elif n > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            with open(
                sys.argv[1],
                "r"
                # f"/Users/999isuru/repos/cs50p/week6/pizza/{sys.argv[1]}", "r"
            ) as file:
                reader = csv.DictReader(file)
                for row in file:
                    rows.append(row.rstrip().split(","))

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        header = rows[0]
        rows.pop(0)
        print(tabulate(rows, header, tablefmt="grid"))


#  need to create a dict of a dict
# with each first word being a the list key and w

if __name__ == "__main__":
    main()
