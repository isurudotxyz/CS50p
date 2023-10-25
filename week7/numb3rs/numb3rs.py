import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    split_ip= ip.split(".")
    
    if re.search(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$",ip) and 0 <= int(split_ip[0]) <= 255 and 0 <= int(split_ip[1]) <= 255 and 0 <= int(split_ip[2]) <= 255 and 0<= int(split_ip[3])<= 255  :
        return True
    else:
        return False
    



if __name__ == "__main__":
    main()
