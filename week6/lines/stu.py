import csv

name = input("name?")
home = input("home?")


with open("stu.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])

    writer.writerow({"name": name, "home": home})
