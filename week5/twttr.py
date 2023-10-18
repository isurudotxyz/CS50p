def main():
    user_prompt = input("Input: ")
    shorten_prompt = shorten(user_prompt)
    print(f"Output: {shorten_prompt}")


def shorten(word):
    output = word
    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            output = output.replace(i, "")
    return output


if __name__ == "__main__":
    main()


# prompt user for a input
