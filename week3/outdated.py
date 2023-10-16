#  middle endian order => mm/dd/yyyy
#  iso 8601 => yyyy-mm-dd
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# prompt user for date in middle endian order 
while True:
    date = input("Date: ").strip()
    try:
        if "," in date:
            date = date.replace(", "," ")
            month,day,year = date.split(" ")
            month = months.index(month) + 1
        # act like month is not integer
        elif "/" in date:
            date = date.replace("/"," ")
            month,day,year = date.split(" ")
        if  int(month) > 12 or int(day) > 31:
            raise ValueError
        
    except (ValueError, KeyError , TypeError, NameError):
        pass
        
    else:
        print(f"{int(year):04}-{int(month):02}-{int(day):02}")
        break
            
        #act like month is an integer
        


#  if month is not a number between 1 and 12 or inside the list 

# convert and print it to iso 8601 