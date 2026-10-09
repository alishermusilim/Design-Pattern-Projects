from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    @abstractmethod
    def show_info(self):
        pass

class Dog(Animal):
    def show_info(self):
        print(f'My dog {self.name} is a {self.breed}')

class Cat(Animal):
    def show_info(self):
        print(f'His cat {self.name} is a {self.breed}')

class Vehicle(ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    @abstractmethod
    def show_info(self):
        pass

class Car(Vehicle):
    def show_info(self):
        print(f'Her {self.name} car was made in {self.year}')

class Gadget(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    @abstractmethod
    def show_info(self):
        pass

class Phone(Gadget):
    def show_info(self):
        print(f'My {self.name} is a brand new {self.model}')
        
class Watch(Gadget):
    def show_info(self):
        print(f'My {self.name} is a {self.model}')


my_dog = Dog("Max", "Golden Retriever")
his_cat = Cat("Meow", "Siamese")
her_car = Car("Toyota", "2024")
my_phone = Phone("IPhone", "IOS27")
my_watch = Watch("Watch", "Smart Watch")


all_items = [my_dog, his_cat, her_car, my_phone, my_watch]

for item in all_items:
    item.show_info()
