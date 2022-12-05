# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negatice.")
#         self.price = value


# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         self.weight = 2

#     def walk(self):
#         print("swim")


# class Fish(Animal):

#     def swim(self):
#         print("swim")


# m = Mammal()
# print(m.weight)
# print(m.age)

# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):

#     def __init__(self):
#         self.opened = False

#     def open(self):

#         if self.opened:
#             raise InvalidOperation("Stream is already running.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file.")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network.")


# class MemoryStream(Stream):
#     def read(self):
#         print("Memory read.")


# stream = MemoryStream()
# stream.open()

# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(x=1, y=2)
# p2 = Point(x=1, y=2)

# print(p1 == p2)

# from sales import calc_shipping, calc_tax
# # import sales
# # sales.calc_shipping()
# calc_shipping()
# calc_tax()

# from ecommerce import sales

# sales.calc_shipping()
# sales.calc_tax()

# print(dir(sales))


from pathlib import Path

# path = Path()


# paths = [p for p in path.iterdir() if p.is_dir()]
# # print(paths)

# py_files = [p for p in path.glob("**/*.py")]
# print(py_files)

path = Path("ecommerce/__init__.py")

print(path.exists())
