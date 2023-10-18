import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
arg_count = len(sys.argv)
try:
    # if cla == 0 input should be in a random font
    if arg_count == 1:
        figlet.setFont(font=random.choice(fonts))
    # if cla == 2 and cla[1] == "-f or --font"select font
    elif arg_count == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
    else:
        raise KeyError

except KeyError:
    sys.exit("Invalid usage")
else:
    s = input("Input: ")
    print(f"Output: {figlet.renderText(s)}")

# hints

#  access font list
# figlet.getFonts()

# set font
# figlet.setFont(font=f)

# output text
# print(figlet.renderText(s))
