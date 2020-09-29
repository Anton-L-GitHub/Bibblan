from datetime import datetime

from utils.lib import Libary

""" Mediatype module concerned with """


class Media:

    def __init__(self, title, creator, length, purchase_price, purchase_year):
        self.title = title
        self.creator = creator
        self.length = length
        self.purchase_price = purchase_price
        self.purchase_year = purchase_year

    @property
    def age(self):
        return datetime.today().year - int(self.purchase_year)

    def __repr__(self):
        return f'{self.title} - {self.creator}'  # DB function?


class Book(Media):
    def __init__(self, title, creator, length, purchase_price, purchase_date):
        super().__init__(title, creator, length, purchase_price, purchase_date)

    @property
    def value(self):
        if int(self.age) >= 50:
            price_today = int(self.purchase_price) * 0.9 ** 50
            price_today = price_today * 1.08 ** (self.age - 50)
            return round(price_today)
        else:
            price_today = int(self.purchase_price) * 0.9 ** int(self.age)
            return round(price_today)


class Movie(Media):
    def __init__(self, title, creator, length, purchase_price, purchase_date):
        super().__init__(title, creator, length, purchase_price, purchase_date)

    @property
    def value(self):
        price_today = self.purchase_price * 0.9 ** self.age
        return round(price_today)


class Cd(Media):
    all_cds = []

    def __init__(self, title, creator, length, purchase_price, purchase_date):
        super().__init__(title, creator, length, purchase_price, purchase_date)
        Cd.all_cds.append(self)

    @property
    def value(self):
        for
