import re
import sys

# problem points
# implement function convert that expect a str in the format
# 9:00 AM to 17:00 PM (am & pm capitalized)
# if the input is not in these format or time is invalid raise and error 



def main():
    print(convert(input("Hours: ")))


def convert(s):
    if search := re.search(r"^(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)$",s):
        # from timing
        hr_from = search.group(1)
        minutes_from = search.group(2)
        meridiem_from = search.group(3)
        # to timing
        hr_to = search.group(4)
        minutes_to = search.group(5)
        meridiem_to = search.group(6)
        
        time1 = transformer(hr_from,minutes_from,meridiem_from)
        time2 = transformer(hr_to,minutes_to,meridiem_to)

        return(f"{time1} to {time2}")
    else:
        raise ValueError


def transformer(h,min,mer):
    if h == "12":
        if mer == "AM":
            h = "00"
        else:
            h = 12
    else:
        if mer == "PM":
            h = int(h) + 12
        else:
            h = int(h)

    if min == None:
        min = "00"
    else:
        min =  int(min)
    
    return f"{int(h):02d}:{int(min):02d}"
    




if __name__ == "__main__":
    main()