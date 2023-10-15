# prompt user for a input 
input = input("Input: ")
output = input

# replace vowels with an empty string
for i in input:
   if i.lower() in ['a','e','i','o','u']:
      output = output.replace(i,"")
# print output
print(f"Output: {output}")
