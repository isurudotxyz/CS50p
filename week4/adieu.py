# create a program that prompt user for names until command d
#  one name per line with at least one name
# each name should be separated with a comma beside the last ne which should be output with an and
import inflect

p = inflect.engine()


def main():
    # prompt user
    get_names()
    ...


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip()

        except EOFError:
            print_names(names)
            break
        else:
            names.append(name)


def print_names(names):
    print("Adieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
