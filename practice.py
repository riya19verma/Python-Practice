class human:
    #constructor
    #to create default constructor use default values
    def __init__(self,name = "X",age = 19): #double underscore with init
        self.name = name
        self.age = age
        
    def greet(self): #self is similar to this in c++
        print(f"Hii {self.name}!!")
        
class women(human): #putting in bracket shows inheritance
    #constructor
    def __init__(self,name,age,husband):
        human.name = name
        human.age = age
        women.husband = husband

    def husb(self):
        print(f"Hello {women.husband}")

human1 = women("Priyanka", 49,"Nick")
human1.greet()#inherites from human class
human1.husb()

#ENCAPSULATION
#In Python, there’s no strict private keyword, but you can use
#underscores to signal intent.
class Car:
    def __init__(self, brand):
        self.__brand = brand  # Private attribute

    def get_brand(self):
        return self.__brand

car = Car("Toyota")
# print(car.__brand)  # AttributeError
print(car.get_brand())  # Toyota

#POLYMORPHISM
class male(human):
    def greet(self):
        print("Good morning Sir")

class female(human):
    def greet(self):
        print("Good morning Madam")

def greet_human(human):
    human.greet()

greet_human(male())  
greet_human(female())

#DECORATOR
#A decorator is essentially a function that takes another function as an
#argument and returns a new function with enhanced functionality.

def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator #equivalent to : say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()

# *args -> poistional argument : When we use * we can pass any number of
#positional arguments, and Python collects them into a tuple
# **kwargs -> keyword argument : When we use ** we can pass any number of
#keyword arguments (like name=value), and Python collects them into a dictionary
def log(func):
    def wrapper(*args, **kwargs): 
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 4))  # Logs: Calling add, then returns 7

from abc import ABC, abstractmethod #ABC is the base class for abstract classes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No implementation here

    @abstractmethod
    def perimeter(self):
        pass
#The @abstractmethod decorator
# ->It marks the method as abstract.
# ->Any class that inherits from Shape must implement these methods.
# ->If a subclass doesn’t implement them, it too becomes abstract
#   and can’t be instantiated.

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
rect = Rectangle(4, 5)
print(rect.area())      # 20
print(rect.perimeter()) # 18

#way to create Docstring
"""
THIS IS
A MULTILINE
DOCSTRING
"""


from typing import List, Dict
#Imports type hints from the typing module:
# ->List: A type hint for a list (like List[int], List[str])
# ->Dict: A type hint for a dictionary (like Dict[str, int])
#Type hints are a way to annotate the types of variables,function arguments,
#   and return values in Python code. They don't affect how the program runs
class BaseScraper(ABC):
    @abstractmethod
    async def fetch_data(self, raw_data:str) -> List[Dict]:
#     |                         |                 |
#asynchronous method    raw_data is a string    returns a list of dictionaries
        pass

#ASYNCHRONOUS FUNCTION
#Synchronous code:
#   One task runs at a time, blocking the program until it’s done.
#Asynchronous code:
#   Tasks can pause (e.g., waiting for network data) and let other tasks run
#   in the meantime. This doesn’t block the entire program!
# Inside an async function, use await to pause until another coroutine or
# async task is done


#AIOHTTP module
#Part	                  Meaning / Use
#async def	          Defines an asynchronous function (coroutine).
#async with	          Async context manager for safe resource handling.
#await	                  Waits for an async operation to complete.
#aiohttp.ClientSession	  HTTP session for efficient requests.
#asyncio.gather(*tasks)	  Runs multiple async tasks concurrently.
