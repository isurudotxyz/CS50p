def main():
    user_prompt = input("What time is it? ").strip()
    time = convert(user_prompt)
    if 7.0 <= time <= 8.0:
       print("breakfast time")
    elif 12.0 <= time <= 13.0:
       print("lunch time")
    elif 18.0 <= time <= 19.0:
       print("dinner time")
    else:
       return
    
    
    


def convert(time):
    h , m = time.split(':')
    h = float(h)
    m = float(m) / 60
    return float(h + m)


if __name__ == "__main__":
    main()