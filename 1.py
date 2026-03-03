# create a class with the name mydictionary and it shoud containds a methods like add items ,update items ,delete items and display items 
# when the object is created empty dictionary should create automaticaly 
# addd items method accepts two parameters key and value ,if the key and value is not present add it to dictionary, if it is already present no need to add
# when update item is called need to pass two paraemeters key and value,if key is already present modify the value if it is not present no need to do any changes
# delete items method acept only one parameter caled key ,if the key is present delete the key and value pair,if the key is not present no need to delete

class mydictionary:
    def __init__(self):
        self.d1={}
    def add_items(self,k,v):
        if k not in self.d1:
            self.d1[k]=v
    def delete_items(self,k):
        if k in self.d1:
            del self.d1[k]
    def update_items(self,k,v):
        if k in self.d1:
            self.d1[k]=v
    def display_items(self):
        print(self.d1)
obj=mydictionary()
obj.add_items(1,"sabi")
obj.add_items(2,"sasi")
obj.add_items(3,"sawi")
obj.delete_items(3)
obj.update_items(2,"soosi")
obj.display_items()