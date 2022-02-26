#Admin script

class Stock:
    def __init__(self,products):
        self.products=products

    def add_product (self,product):
        self.products.append(product)

    #SQL upit ---> dodati u bazu podataka

    def get_price (self,name):
        #SQL baza podataka- dohvatiti proizvod kojem je ime == name !

        for p in self.products:
            if p.ime == name:
                return p.price - p.discount * p.price

   # print("Desired product does not exist!")

    def delete_product (self,id):
        for pr in self.products:
            if pr.id == id:
                self.products.remove(pr)
                break

    def total_products (self,products):
        return len(self.products)

    def name_update (self,id,new_name):
        for pr in self.products:
            if pr.id == id:
                pr.change_name(new_name)
                break

    def total_product_list(self,collection):
        final=[]
        for p in self.products:
            if p.collection == collection:
                final.append(p)
        return final

class Product:
    def __init__(self, id, name, price, collection):
        self.name = name
        self.id = id
        self.price = price
        self.collection = collection

    def change_name(self, new_name):
        self.name = new_name


def main():
#Pocetni dio
    warehouse=Stock(products=[])
    product1=Product(id=1,name='Product name',price=10,collection='Collection name')
    warehouse.add_product(product1)

# for the next phase we will update this to be in SQL local server

if __name__ == '__main__':
    main()
