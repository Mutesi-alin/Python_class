class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def produce(self):
        pass
class Bird(Animal):
    def make_sound(self):
        print("chirp")

    def move(self):
        print("fly")
    def produce(self):
        print("lay eggs")
class Fish(Animal):
    def make_sound(self):
        print("click")
    def move(self):
        print("swimming")
    def produce(self):
        print("lay eggs")

class Dog(Animal):
    def make_sound(self):
        print("bark")
    def move(self):
        print("running")
    def produce(self):
        print("produce there young ones")  
class Human(Animal):
    def make_sound(self):
        print("talk")
    def move(self):
        print("walk")
    def produce(self):
        print("produce there young ones")