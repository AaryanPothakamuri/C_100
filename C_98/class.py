class Car (object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")  
        
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerated")
        "accelerating functionality over here "
        
    def change_gear(self,gear_type):
        print("gear shifted")
        "gear functionality over here"

audi=Car("R8", "Black" , "Audi", "205")
print(audi.change_gear(1))