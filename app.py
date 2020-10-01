from utils.lib import Libary
from utils.prompt import USER_CHOICE, add_item, print_items

""" Main moudule for application """


def main():
    libary = Libary()
    user_input = input(USER_CHOICE)
    while user_input != '0':
        if user_input == '1':
            add_item(libary)
        elif user_input == '2':
            print_items(libary)
        elif user_input == '3':
            libary.save_to_disc()
        elif user_input == '4':
            pass
        user_input = input(USER_CHOICE)
    libary.save_to_disc()


if __name__ == '__main__':
    main()
