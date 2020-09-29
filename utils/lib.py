import inspect

from .data.database import disk_get, disk_save
from .mediatypes import Book, Movie, Cd
from .prompt import media_args

""" Lib module concerned with """


class Libary:
    def __init__(self):
        self.lib_list = []
        self._init_from_disk()

    def add_item(self, obj_cls, args):
        new_obj = obj_cls(*args)
        self.lib_list.append(new_obj)

    def get_items(self, sort_by):
        items = self.lib_list
        if sort_by == '1':  # Sort by added
            return items
        elif sort_by == '2':  # Sort by title
            return sorted(items, key=lambda x: x.title)
        elif sort_by == '3':  # Sort by value
            return sorted(items, key=lambda x: x.value)

    def _init_from_disk(self):
        items = disk_get()
        for item in items:
            if item['type'] == 'Book':
                keys = [item[key] for key in item.keys()][1:]
                self.add_item(Book, keys)
            elif item['type'] == 'Movie':
                keys = [item[key] for key in item.keys()][1:]
                self.add_item(Movie, keys)
            elif item['type'] == 'Cd':
                keys = [item[key] for key in item.keys()][1:]
                self.add_item(Cd, keys)

    def save_to_disk(self):
        all_obj = []
        for obj in self.lib_list:
            obj_dict = {}
            args = media_args(obj.__class__)
            values = [i for i in obj.__dict__.values()]
            obj_dict['type'] = obj.__class__.__name__  # Add object class -> obj_dict
            for arg, value in zip(args, values):  # Add objects other key value pairs -> obj_dict
                obj_dict[str(arg)] = str(value)
            all_obj.append(obj_dict)
        disk_save(all_obj)
