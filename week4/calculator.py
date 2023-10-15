def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n
  
if __name__ == "__main__":  
    main()