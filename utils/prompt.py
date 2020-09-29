import inspect  # python 3.3

from utils.mediatypes import Book, Movie, Cd

""" Prompt module concerned with input/utput in terminal """

USER_CHOICE = """
Type:
    1. Add media to library
    2. List media
    3. Save
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
    4. Media Type
    -> """


def add_item(libary):  # Borde vara en funktion i prompt
    cls_wanted = media_type()
    args = [input(f'{arg}:') for arg in media_args(cls_wanted)]
    return libary.add_item(cls_wanted, args)


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


def media_args(cls):
    return inspect.getfullargspec(cls.__init__)[0][1:]
