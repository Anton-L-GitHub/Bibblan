import inspect

from utils.mediatypes import Book, Movie, Cd

""" Concerned with input/utput in terminal """

USER_CHOICE = """
Type:
    1. Add media to library
    2. List media
    --
    0. Exit
    
    -> """

MEDIA_CHOICE = """
    1. Book
    2. Movie
    3. CD
    -> """

SORT_CHOICE = """List media sorted by...
    1. Added
    2. Title
    3. Todays value | Lowest -> Highest
    --
    0. Tillbaka
    -> """


def add_item(libary):
    try:
        cls_wanted = media_type()
        args = [input(f'{arg.replace("_", " ").capitalize()}: ') for arg in media_args(cls_wanted)]
        return libary.add_item(cls_wanted, args)
    except ValueError:
        print('Check input and try again!')


def media_type():
    """ Input-prompt with different media classes, returns user-selected class """
    media_choice = input(MEDIA_CHOICE)  # Kolla input
    while media_choice != '0':
        if media_choice == '1':
            return Book
        elif media_choice == '2':
            return Movie
        elif media_choice == '3':
            return Cd
        media_choice = input(MEDIA_CHOICE)


def print_items(libary):
    sort_choice = input(SORT_CHOICE)
    while sort_choice != '0':
        try:
            for item in libary.get_items(sort_choice):
                print(item)
            break
        except TypeError:
            sort_choice = input(SORT_CHOICE)


def _print_items(list_of_dict):
    for item in list_of_dict:
        print(item)


def media_args(cls):
    return inspect.getfullargspec(cls.__init__)[0][1:]
