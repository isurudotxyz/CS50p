import validators


def main():
    email = input("What's your email address?")
    email_validation = validators.email(email)
    if email_validation == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()

    