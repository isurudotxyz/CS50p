import sys
bankPrompt = input("Greeting: ").lower()

if "hello" in bankPrompt:
   print("$0",end="")
   sys.exit()
elif bankPrompt[0] == "h":
   print("$20",end="")
   sys.exit()
else:
   print("$100", end="")
   sys.exit()
   
   
   

