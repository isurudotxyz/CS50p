import sys

str = input("Camel case: ")
output = ""

for i in str:
    if i.isupper():
         output += "_" + i.lower()
    else:
         output += i
print(f"snake_case: {output}")

  
