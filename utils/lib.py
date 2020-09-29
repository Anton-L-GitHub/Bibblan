from .data.database import disk_get, disk_save
from .mediatypes import Book, Movie, Cd

""" Lib module concerned with """


class Libary:
    def __init__(self):
        self.lib_list = []
        self._init_from_disk()

    def add_item(self, obj_cls, args):
        new_obj = obj_cls(*args)
        self.lib_list.append(new_obj)

    def print_items(self):
        for item in self.lib_list:
            print(item)  # skapa snygg funktion i prompt? lägg till att den skall visa allt + value

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
            all_obj.append(
                {'type': obj.__class__.__name__, 'title': obj.title, 'creator': obj.creator, 'length': obj.length,
                 'purchase_price': obj.purchase_price, 'purchase_year': obj.purchase_year})
        disk_save(all_obj)
