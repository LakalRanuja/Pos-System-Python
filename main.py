import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__item_folder__ = f"{__db_location__}/item"
__item__last_id__ = f"{__db_location__}/item_id.db"
__customer_folder__ = f"{__db_location__}/customer"
__customer_last_id__ = f"{__db_location__}/customer_id.db"
__order_folder__ = f"{__db_location__}/order"
__order_last_id__ = f"{__db_location__}/order_id.db"


def init(arguments):

    def db():
        os.makedirs(__item_folder__)
        os.makedirs(__customer_folder__)
        os.makedirs(__order_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view():
    username = __get_logged_user()
    print(username)


def login(username):
    f = open(__session_file__, "w")
    f.write(username)
    f.close()


class Customer:
    def __init__(self):
        if os.path.exists(__customer_last_id__):
            with open(__customer_last_id__, "r") as last_id_c:
                self.last_id = int(last_id_c.readline())
        else:
            self.last_id = 0

    def saveCustomer(self):
        cusID = self.last_id+1

        # Save Customer in database
        _data_ = {
            "cusId": cusID,
            "cusName": self.cusName,
            "cusAddress": self.cusAddress,
            "cusContact": self.cusContact
        }
        with open(f"{__customer_folder__}/{cusID}.db", "w") as customer_file:
            json.dump(_data_, customer_file)

        # Save next id
        self.last_id += 1
        with open(__customer_last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        Customer.__get_customer_by_path(self, f"{__customer_folder__}/{id}.db")

    def __get_customer_by_path(customer, path):
        with open(path, "r") as customer_file:
            _data_ = json.load(customer_file)
            customer.cusId = _data_["cusId"]
            customer.cusName = _data_["cusName"]
            customer.cusAddress = _data_["cusAddress"]
            customer.cusContact = _data_["cusContact"]

    def all(self):
        customer_file_names = os.listdir(__customer_folder__)
        customers = []
        for customer_file_name in customer_file_names:
            customer = Customer()
            Customer.__get_customer_by_path(
                customer, f"{__customer_folder__}/{customer_file_name}")
            customers.append(customer)
        return customers

    def __repr__(self):
        return f"cusId:{self:cusId},cusName:{self.cusName},cusAddress:{self.cusAddress},cusContact:{self.cusContact}"

    def __str__(self):
        return f"cusId:{self:cusId},cusName:{self.cusName},cusAddress:{self.cusAddress},cusContact:{self.cusContact}"


def customer_create(cusName, cusAddress, cusContact):
    customer = Customer()
    customer.cusName = cusName
    customer.cusAddress = cusAddress
    customer.cusContact = cusContact
    customer.saveCustomer()


def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)


def customer_view(id):
    customer = Customer()
    customer.find(id)
    print(customer.cusId, customer.cusName,
          customer.cusAddress, customer.cusContact)


class Order:
    def __init__(self):
        if os.path.exists(__order_last_id__):
            with open(__order_last_id__, "r") as last_id_o:
                self.last_id = int(last_id_o.readline())
        else:
            self.last_id = 0

    def saveOrder(self):
        oid = self.last_id+1

        # Save Order in Database
        _data_ = {
            "oid": oid,
            "cusid": self.cusid,
            "itemid": self.itemid,
            "itemname": self.itemname

        }
        with open(f"{__order_folder__}/{oid}.db", "w") as order_file:
            json.dump(_data_, order_file)

        # Save next id
        self.last_id += 1
        with open(__order_last_id__, "w") as f:
            f.write(str(self.last_id))

        def find(self, id):
            Order.__get_order_by_path(self, f"{__order_folder__}/{id}.db")

        def __get_order_by_path(order, path):
            with open(path, "r") as order_file:
                _data_ = json.load(order_file)
                order.oid = _data_["oid"]
                order.cusid = _data_["cusid"]
                order.itemid = _data_["itemid"]
                order.itemname = _data_["itemname"]

        def all(self):
            order_file_names = os.listdir(__order_folder__)
            orders = []
            for order_file_name in order_file_names:
                order = Order()
                Order.__get_order_by_path(
                    order, f"{__order_folder__}/{order_file_names}")
                orders.append(order)
            return orders


def order_create(cusid, itemid, itemname):
    order = Order()
    order.cusid = cusid
    order.itemid = itemid
    order.itemname = itemname
    order.saveOrder()


def order_all():
    order = Order()
    orders = order.all()
    pprint(orders)


def order_view(oid):
    order = Order()
    order.find(id)
    print(order.oid, order.cusid, order.itemid, order.itemname)


class Item:
    def __init__(self):
        if os.path.exists(__item__last_id__):
            with open(__item__last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        id = self.last_id+1

        # Save item in Database
        _data_ = {
            "id": id,
            "name": self.name,
            "price": self.price,
            "sellingPrice": self.selling_price
        }
        with open(f"{__item_folder__}/{id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        # Save next id
        self.last_id += 1
        with open(__item__last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        Item.__get_item_by_path(self, f"{__item_folder__}/{id}.db")

    def __get_item_by_path(item, path):
        with open(path, "r") as item_file:
            _data_ = json.load(item_file)
            item.id = _data_["id"]
            item.name = _data_["name"]
            item.price = _data_["price"]
            item.selling_price = _data_["sellingPrice"]

    def all(self):
        item_file_names = os.listdir(__item_folder__)
        items = []
        for item_file_name in item_file_names:
            item = Item()
            Item.__get_item_by_path(
                item, f"{__item_folder__}/{item_file_name}")
            items.append(item)
        return items

    def search(self, key, value):
        items = self.all()
        result_items = []
        for item in items:
            item_value = getattr(item, key)
            if item_value == value:
                result_items.append(item)
        return result_items

    def __repr__(self):
        return f"id:{self.id},name:{self.name},price:{self.price}"

    def __str__(self):
        return f"id:{self.id},name:{self.name},price:{self.price}"


def item_create(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()


def item_all():
    item = Item()
    items = item.all()
    pprint(items)


def item_view(id):
    item = Item()
    item.find(id)
    print(item.id, item.name, item.price, item.selling_price)


def item_search(key, value):
    item = Item()
    results = item.search(key, value)
    pprint(results)


if __name__ == "__main__":
    arguments = sys.argv[1:]

    init(arguments)

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "login":
            login(*params)
        elif command == "view":
            view()

    # Customer
    elif section == "customer":
        if command == "create":
            customer_create(*params)
        elif command == "all":
            customer_all()
        elif command == "view":
            customer_view(*params)

    #  Order
    elif section == "order":
        if command == "create":
            order_create(*params)
        elif command == "all":
            order_all()
        elif command == "view":
            order_view(*params)

    # Items
    elif section == "item":
        if command == "create":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
        elif command == "search":
            item_search(*params)
