import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if html := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{html.group(2)}"



if __name__ == "__main__":
    main()