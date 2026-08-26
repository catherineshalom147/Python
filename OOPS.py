''' 
OOPS - object oriented programming language consists of objects and classes
class is a blueprint, variables are attributes, functions are behaviours
'''

# basic programm
class basic: # creating a class
    def function(self): # creating a function ( parameter self is passed when the inputs are unkown)
        print("you are inside the function") 
object = basic()  # storing the class into a variable
object.function() # calling the function

# 1. class - it is a blueprint 
class employee:
    employee_id = 101
    employee_name = "Alia"
s = employee()
print(s.employee_name)

# 2. object - are instance of class
# in the above program - s is the object

# 3. constructor - is a default function where objects directly access the function
class entity:
    breed = "poodle"
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
obj = entity("animals",10)
print(obj.name)
print(obj.quantity)
print(obj.breed)

'''
 instance variables - self is instance variable that refers to current object
 class variables - defined inside a class, the variable can be accessed by all objects
 methods  - are functions defined inside a class
 - types : instance method, class method, static method
 '''

# 4. encapsulation - accessing data and methods are accessed
# public, _private, __protected - variables can be defined with following types of access
class eduction:
    def __init__(self,course):
        self.course = course
    def teacher(self,name,course_id):
        self.name = name
        self.course += course_id
    def student(self):
        print(self.course)
obj = education()

# 5. Inheritence - allows to access methods and properties of another class
class Animal:
    def predator(self):
        print("huntingggg...........")
class Dog(Animal):
    def bark(self):
        print("barkinggggg..........")
obj = Animal()
obj.predator()
obj.bark()
