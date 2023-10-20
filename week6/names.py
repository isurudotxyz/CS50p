name = input("What's your name")
# open file to read or write information into in it
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    file.close()
