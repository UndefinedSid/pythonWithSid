class Demo:
    company = "Google"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable
        print("Hello", self.name)

d1 = Demo("Sid")    # Creating object of Demo class
print(Demo.company) # Accessing class variable
print(d1.name)      # Accessing instance variable

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):  #__str__() method to return string representation
        return self.title

b = Book("Python")
print(b)    # Output: Python


# OOPs Concepts in Python

class Student:
    def __init__(self, name, age):   #  __init__() constructor
        self.name = name
        self.age = age

    def show(self): # self is used to access instance variables
        print(self.name, self.age)

s1 = Student("Sid", 20)
s1.show()

# Encapsulation Example
# public -> balance , protected -> _balance , private -> __balance
class Bank:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.deposit(1000)
b.show_balance()

# Inheritance Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()   # Output: Dog barks     
a = Animal()
a.speak()   # Output: Animal speaks

#mutiple inheritance
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")   

class C(A, B):
    def method_c(self):
        print("Method C")

c = C()
c.method_a()    # Call method from class A
c.method_b()    # Call method from class B
c.method_c()    # Call method from class C

# Polymorphism Example(many forms)

# Method Overriding Example
class Cat:
    def speak(self):
        print("Cat meows")
class Cow:
    def speak(self):
        print("Cow moos")
    def animal_sound(animal):
        animal.speak()

objects = [Cat(), Cow()]
for obj in objects:
    obj.speak()  # Calls the appropriate speak() method based on the object type

# Method Overloading Example
class MathOperations:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c
    
math = MathOperations()
print(math.add(2, 3))        # Output: 5
print(math.add(2, 3, 4))     # Output: 9

# Abstraction Example
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50

# Abstract class cannot be instantiated
# shapes = Shape()  # This will raise an error





