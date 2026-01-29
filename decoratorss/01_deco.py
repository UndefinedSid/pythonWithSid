def decorator(func): #func is say_hello
    def wrapper():
        print("before function call")
        func()  #say_hello()
        print("after function call")
    return wrapper  #returning wrapper function

@decorator  #say_hello = decorator(say_hello)
def say_hello():
    print("hello")

say_hello()
# Output:
# before function call
# hello
# after function call

# Without decorator syntax
# def say_hello():
#     print("hello")    
# say_hello = decorator(say_hello)


def decorator_with_args(func):
    def wrapper(*args, **kwargs):   #wrapper can take any number of arguments by using *args and **kwargs
        print("before function call")
        res=func(*args, **kwargs)   #
        print("after function call")
        return res
    return wrapper

@decorator_with_args
def greet(name,sub):
    print(f"Hello, {name} ! {sub}")   
greet("SID","Welcome to Python decorators.")
# Output:
# before function call
# Hello, SID!
# after function call


def dec_with_param(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator parameter: {param}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@dec_with_param("Custom parameter")
def display(message):
    print(message)
display("example of decorator with custom parameter")
# Output:
# Decorator parameter: Custom parameter
# example of decorator with custom parameter

# @staticmethod -> built in decorator in python
def static_decorator(func):
    def wrapper(*args, **kwargs):
        print("Static method decorator")
        return func(*args, **kwargs)
    return wrapper  
@static_decorator
def static_example():
    print("Inside static example function")
static_example()
# Output:
# Static method decorator
# Inside static example function

#   @classmethod -> built in decorator in python
def class_decorator(func):
    def wrapper(cls, *args, **kwargs):
        print("Class method decorator")
        return func(cls, *args, **kwargs)
    return wrapper  
@class_decorator
def class_example(cls):
    print("Inside class example function")
class_example("MyClass")
# Output:
# Class method decorator    
# Inside class example function

# @property -> built in decorator in python
def property_decorator(func):
    def wrapper(self):
        print("Property decorator")
        return func(self)
    # return wrapper  #returning wrapper function
    return property(wrapper)  # returning a property object

class MyClass:
    def __init__(self, value):
        self._value = value

    @property_decorator
    def value(self):
        return self._value  

obj = MyClass(10)
print(obj.value)
# Output:
# Property decorator
# 10    

class Myproperty:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        print("Getting value using custom property")
        return self.fget(instance)  
    
    def __set__(self, instance, value): 
        print("Setting value using custom property")
        instance._value = value
    
    def __delete__(self, instance):
        print("Deleting value using custom property")
        del instance._value

    def setter(self, fset):
        self.fset = fset
        return self

class AnotherClass:
    def __init__(self, value):
        self._value = value

    @Myproperty
    def value(self):
        return self._value  

    @value.setter
    def value(self, new_value):
        if(new_value < 0):
            raise ValueError("Value cannot be negative")
        self._value = new_value

obj = AnotherClass(20)
print(obj.value)  # Getting value using custom property \n 20
obj.value = 30    # Setting value using custom property
print(obj.value)  # Getting value using custom property \n 30   
# Output:
# Getting value using custom property
# 20
# Setting value using custom property
# Getting value using custom property
# 30







