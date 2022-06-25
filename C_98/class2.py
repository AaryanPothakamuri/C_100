class Shoes(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def launch(self):
        print("launched")
    
    def new_collection(self, collection_size):
        print("collection started")

Air_Jordan=Shoes("Nike", "Red")
print(Air_Jordan.brand)
Yeezys=Shoes("Adidas", "White")
print(Yeezys.color)