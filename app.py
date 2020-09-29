from utils.lib import Libary
from utils.prompt import USER_CHOICE, add_item


def main():
    libary = Libary()
    user_input = input(USER_CHOICE)
    while user_input != '0':
        if user_input == '1':
            add_item(libary)
        elif user_input == '2':
            libary.print_items()
        elif user_input == '3':
            libary.save_to_disk()
        elif user_input == '4':
            pass
        user_input = input(USER_CHOICE)
    libary.save_to_disk()


if __name__ == '__main__':
    main()
