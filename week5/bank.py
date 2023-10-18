def main():
    user_prompt = input("Greeting: ")
    output = value(user_prompt)
    print(f"${output}")


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
