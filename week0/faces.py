  
def convert(input):
    return (input.replace(":)","🙂").replace(":(","🙁"))

def main():
   str = input()
   output = convert(str)
   print(output)

main()