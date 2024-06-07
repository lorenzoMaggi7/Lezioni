# """
# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
# """
from abc import ABC, abstractmethod
import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass



# class Rectangle(Shape):

#     def __init__(self,width, height):
#         self.width = width
#         self.height = height 

#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2*(self.widht+self.height)
    

# class Circle(Shape):

#     def __init__(self, raggio):
#         self.raggio = raggio


#     def area(self):
#         return math.pi * self.raggio **2
    
#     def perimetro(self):
#         return 2 * math.pi *self.raggio

# circle = Circle(5)
# print(f"Circle area: {circle.area()}")
# print(f"Circle perimeter: {circle.perimeter()}")

# rectangle = Rectangle(4, 7)
# print(f"Rectangle area: {rectangle.area()}")
# print(f"Rectangle perimeter: {rectangle.perimeter()}")


"""
    Exercise 2: Implementing Static Methods

    Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
    and another static method multiply that takes two numbers and returns their product.
"""

class MathOperations:

    @abstractmethod
    def sum(a, b):
        return a+b
    
    @abstractmethod
    def multiply(a, b):
        return a * b
    

result_add= MathOperations.sum(10, 20)
print(f"La somma dei numeri è: {result_add}")
result_multiply = MathOperations.multiply(15, 25)
print(f"La moltiplicazione tra i due numeri fa: {result_multiply}")
