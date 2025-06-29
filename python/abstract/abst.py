# from abc import ABC, abstractmethod
# class Animal(ABC):  # Animal is an abstract class

#     @abstractmethod
#     def make_sound(self):
#         pass  # no implementation here
# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
# dog = Dog()
# cat = Cat()

# print(dog.make_sound())  # Bark
# print(cat.make_sound())  # Meow
# def animal_sound(animal: Animal):
#     print(animal.make_sound())

# animal_sound(Dog())
# animal_sound(Cat())

from abc import ABC, abstractmethod
#here abc-Abstract Base Classes and from these classes
#we are importing ABC - Abstract Base Class

class Car(ABC):  # here car is abstract class
# an abstrat class is the class that cant be initialize 
# direcly instead it meant to be inherited 
# by other class
    @abstractmethod
#An abstract method is a method that is declared without 
# an implementation — meaning it has no body
    def model(self):
        pass

class Tata(Car):
    def model(self):
        return "Curvv"
    
class Mahindra(Car):
    def model(self):
        return "Scarpio"
    
a = Tata()
b = Mahindra()

print(a.model())
print(b.model())
