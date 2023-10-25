import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    regex = r"^um\b|(?<=\s)um\b"
    if n := re.findall(regex,s,re.IGNORECASE):
        return len(n)


if __name__ == "__main__":
    main()