from datetime import datetime

""" Mediatype module concerned with """


class Media:
    """ Represents a basic media struture for the libary """

    def __init__(self, title, creator, length, purchase_price, purchase_year):
        self.title = title
        self.creator = creator
        self.length = length
        self.purchase_price = purchase_price
        self.purchase_year = purchase_year

    @property
    def age(self):
        return datetime.today().year - int(self.purchase_year)

    @property
    def value(self):
        return None

    def __str__(self):
        return f'{"-" * 20}\n{self.__class__.__name__} - {self.title} - Author: {self.creator} - Minutes: {self.length} -' \
               f'Bought: {self.purchase_year} - Year of purchase: {self.purchase_price} - Price Now {self.value}'


class Book(Media):
    def __init__(self, title, creator, length, purchase_price, purchase_year):
        super().__init__(title, creator, length, purchase_price, purchase_year)

    @property
    def value(self):
        if int(self.age) >= 50:
            price_today = float(self.purchase_price) * 0.9 ** 50
            price_today = price_today * 1.08 ** (float(self.age) - 50)
            return round(price_today)
        else:
            price_today = float(self.purchase_price) * 0.9 ** float(self.age)
            return round(price_today)


class Movie(Media):
    def __init__(self, title, creator, length, purchase_price, purchase_year, how_damaged):
        super().__init__(title, creator, length, purchase_price, purchase_year)
        self.how_damaged = how_damaged

    @property
    def value(self):
        price_today = float(self.purchase_price) * 0.9 ** float(self.age)
        price_today = price_today * float(f'0.{self.how_damaged}')
        return round(price_today)


class Cd(Media):
    all_cds = []

    def __init__(self, title, creator, length, purchase_price, purchase_year):
        super().__init__(title, creator, length, purchase_price, purchase_year)
        Cd.all_cds.append(self)

    @property
    def value(self):
        quantity = 0
        for item in Cd.all_cds:
            if self.title == item.title and self.creator == item.creator:
                quantity += 1
        return round(float(self.purchase_price) / quantity)
