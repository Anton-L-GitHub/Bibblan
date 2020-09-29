import inspect

from utils.data.database import disk_get
from utils.mediatypes import Movie


class A(object):
    def __init__(self):
        self.b = 1
        self.c = 2

    def do_nothing(self):
        pass


obj = Movie('asdf', 'asdf', '200', '300', '1999', '9')

values = [i for i in obj.__dict__.values()]

print(values)
