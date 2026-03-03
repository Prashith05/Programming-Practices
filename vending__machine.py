'''
 program using classes and object to create and working functionality of a whenting m/c 
->it should contain an attributes like items and cart 
->methods like display items,display cart ,add to cart and update cart ,total price
->when the object is created it should create an empty cart and it should accept all 
  the items along with its prices
'''

class VendingMachine:
    def __init__(self,products):
        self.products = products
        self.cart = {}
    def display_products(self):
        for k,v in self.products.items():
            print(k," : ",v)
    def display_cart(self):
        print("----- ITEMS IN CART -----")
        if len(self.cart) == 0:
            print("No items in cart")
        else:
            for k, v in self.cart.items():
                print(k," : ",v)
        print()            
    def add_to_cart(self,item,qty):
        if item in self.products:
            if item not in self.cart:
                self.cart[item] = qty
            else:
                self.cart[item] += qty

    def total_price(self):
        res = 0
        for k,v in self.cart.items():
            total = v*self.products[k]
            res += total
            print(k," : ",v,"*",self.products[k],"=",total) 
        print("-"*30)
        print("total price :",res)                                              

products = {
    'kitkat' : 25,
    'oreo' : 30,
    'jimjam': 35,
    'bingo' : 10,
    'chikki' : 15,
    'cupcake':  5,
    'snickers': 15

}
vm = VendingMachine(products)
while True:

    print("LIST OF ALL THE PRODUCTS")
    vm.display_products()
    print()
    print("1.Add to cart\n 2.Display cart\n 3.Total price")
    opt = int(input("enter your option :"))
    match opt:
        case 1:
            item = input("enter the item :")
            qty = int(input("Enter the quantity :"))
            vm.add_to_cart(item,qty)
        case 2:
            vm.display_cart()
        case 3:
            vm.total_price()
            break
        case _:
            print("invalid option")        
