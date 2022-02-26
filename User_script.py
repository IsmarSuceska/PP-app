#User Script
import imaplib
import smtplib
import getpass
from Klasa import Product

class UserStock:
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




def main():
#Pocetni dio
    warehouse=UserStock(products=[])
    product1=Product(id=1,name='Product name',price=10,collection='Collection name')
    warehouse.add_product(product1)


## slj verzija ce proizvode kupiti iz baze


    uslov = True
    while (uslov):
        x = input("Pick an option\n \
                   1. All products\n \
                   2. Purchase products \
                       3. Exit")
    if x == "1":
        list=UserStock.total_products()
        print(list)
    # ....
    if x == "2":
        desired_product= input(' Which product would you like to pruchase? ')
        price=warehouse.get_price(desired_product)
        print(f'Price for {desired_product} is {price}')

        decision=input('Do you want to continue with purchase? Y/N')

        if decision == 'Y':
            delete=Stock.delete_product(desired_product,'5')
            confirmation= input(' Congradulation, please enter your email for purchase confirmaiton? ')
            #Email- should been a different class or script
            smtp_object.starttls()
            smtp_object.ehlo()
            email='myemail@gmail.com'
            password='mypassword'#<--- it would have been protected
            smtp_object.login(email,password)
            from_address=email
            to_address=confirmation
            subject='Order confirmation '
            body= f'Your order for {desired_product} has been confirmed'
            msg='Subject:' +subject+'\n'+body
            smtp_object.sendmail(from_address,to_address,msg)
            smtp_object.quit()
        else:
            break

    else:
        a = input("Unijeli ste pogresan broj, da li zelite zavrsiti? (Y/N)")
    if a == 'Y':
        uslov = False
    else:
        uslov = True 


# for the next phase we will update this to be in SQL local server

if __name__ == '__main__':
    main()
