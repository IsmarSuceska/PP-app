class Product:
    def __init__(self, id, name, price, collection):
        self.name = name
        self.id = id
        self.price = price
        self.collection = collection

    def change_name(self, new_name):
        self.name = new_name
