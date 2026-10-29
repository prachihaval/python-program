
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        l = int(input("Enter length: "))
        b = int(input("Enter breadth: "))
        print("Area of rectangle:", l * b)

obj = Rectangle()
obj.area()











# # Regular Expression in Python

# import re

# text = "virajpotdar4@gmail.com"

# # 1. findall()
# result = re.findall(r"\w+", text)
# print("Findall:", result)


# # 2. compile()
# pattern = re.compile(r"\w+@\w+\.\w+")
# result = pattern.search(text)
# print("Compile:", result.group())


# # 3. split()
# split = re.split(r"@", text)
# print("Split:", split)


# # 4. sub()
# sub = re.sub(r"gmail", "yahoo", text)
# print("Sub:", sub)


# # 5. escape()
# esc = re.escape(text)
# print("Escape:", esc)


# # 6. search()
# result = re.search(r"\w+@\w+\.\w+", text)

# if result:
#     print("Search:", result.group())
# else:
#     print("Search: No match")