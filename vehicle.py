class Vechicle:

    def __init__(self, make,model, color):
        self.make= make
        self.color=color
        self.model=model

    def move(self):
        print("satr moving")
    def hoot(self):
        print("hook hook")   

class Bus(Vechicle):
     def __init__(self,make,model, color,capacity):
         super().__init__(make,model,color) 
         self.capacity= capacity      
     def start_boarding(self):
         print("the bus is now boarding")
class Lorry(Vechicle):

     def __init__(self,make,model, color,max_bod):
           super().__init__(make,model,color) 
           self.max_bod= max_bod
def load(self):
    print("started bording")




    
             
                
    