import sys
import csv

n = len(sys.argv)

try:
    if n > 3:
        sys.exit("Too few command-line arguments ")
    elif n < 3:
        sys.exit("Too many command-line arguments ")
    elif sys.argv[1][-4:] != ".csv" and sys.argv[2][-4:] != ".csv":
        sys.exit("Invalid input")
    else:
        rows = []
        with open(sys.argv[1], "r") as c:
            reader = csv.DictReader(c)
            for line in reader:
                # polish name in 2 output
                last, first = line["name"].split(", ")
                rows.append({"first": first, "last": last, "house": line["house"]})
        with open(sys.argv[2], "w") as p:
            writer = csv.DictWriter(p, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for i in rows:
                l = i["last"]
                f = i["first"]
                h = i["house"]
                writer.writerow({"first": f, "last": l, "house": h})
except FileNotFoundError:
    sys.exit(f"file {sys.argv[1]} not found")
    ...
