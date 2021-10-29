import sys
import pickle
import json

class Item:
    pass

    def save(self):
        _data_ = {
            "name": self.name,
            "price": self.price,
            "selling_price": self.selling_price
        }
        item_file = open(__item_file__, "w")
        json.dump(_data_, item_file)

    def get(self):
        item_file = open(__item_file__,"rb")
        _data_ = json.load(item_file)
        print(_data_)

def item_create(name,price,selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()

def item_All():
    print("All Items")

def item_view(id):
    print("View Item",id)