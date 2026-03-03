# program using classes and object to create and working functionality of a venting m/c 
# ->it should contain an attributes like items and cart 
# ->methods like display items,display cart ,add to cart and update cart ,total price
# ->when the object is created it should create an empty cart and it should accept all the items along with its prices
class VendingMachine:
    def __init__(self, products):
        self.products = products
        self.cart = {}

    def display_products(self):
        print("----- PRODUCTS -----")
        for k, v in self.products.items():
            print(k," : ", v)
        print()
    
    def display_cart(self):
        print("\n----- ITEMS IN CART -----")
        if len(self.cart) == 0:
            print("No items in cart\n")
        else:
            for k, v in self.cart.items():
                print(k," : ",v)
        print()

    def add_to_cart(self, item, qty):
        if item in self.products:
            if item not in self.cart:
                self.cart[item] = qty
            else:
                self.cart[item] += qty
    
    def total_price(self):
        print("\n----- TOTAL PRICE -----")
        res = 0
        for k, v in self.cart.items():
            total = v * self.products[k]
            res += total
            print(k," : ",v," * ",self.products[k], " = ", total)
        print("-" * 30)
        print("Total Price : ",res)
        print()
    
products = {
    'kitkat' : 25,
    'oreo' : 30,
    'jim-jam' : 35,
    'bingo' : 10,
    'chikki' : 15,
    'cupcake' : 5,
    'snickers' : 15
}

vm = VendingMachine(products)
# vm.display_products()
# vm.add_to_cart('kitkat', 5)
# vm.add_to_cart('cupcake', 10)
# vm.add_to_cart('kitkat', 2)
# vm.add_to_cart('lays', 5)
# vm.add_to_cart('snickers', 5)
# vm.display_cart()
# vm.total_price()

# print("List of all products")
vm.display_products()
while True:
    print("1. Add to cart\n2. Display Cart\n3. Total Price")
    opt = int(input("Enter your option: "))
    match opt:
        case 1:
            item = input("Enter the item: ")
            qty = int(input("Enter the quantity: "))
            vm.add_to_cart(item, qty)
        case 2:
            vm.display_cart()
        case 3:
            vm.total_price()
        case _:
            print("Invalid Option")
            break



