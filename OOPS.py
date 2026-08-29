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

# 6. Multiple inheritance - a class inherits other classes into it
class Owner:
    def objective(self):
        print("target is been fixed")
class Manager:
    def performing(self):
        print("they execute the plan")
class Employee(Owner,Manager):
    pass
obj = Employee()
obj.objective()
obj.performing()

# 7. Multilevel inheritence
class Principal:
    def function(self):
        print("manages the school")
class Teacher(Principal):
    def anotherfunc(self):
        print("teacher listens to principal")
class students(Teacher):
    def studfunc(self):
        print("student does the task")
obj = students()
obj.function()
obj.anotherfunc()
obj.studfunc()

# 8. hierrachical inheritence
class humans:
    def func(self):
        print("lives......")
class Singers(humans):
    def func1(self):
        print("sings.........")
class dancers(humans):
    def func2(self):
        print("dances........")
obj = Singers()
obj1 = dancers()
obj.func()
obj.func1()
obj1.func()
obj.func2()

# 9.polymorphism - the function or interface can behave differently based on objects
class Parent:
    def func(self):
        print("father, mother")
class Child:
    def func(self):
        print("children")
obj = Parent()
obj.func()
obj1 = Child()
obj1.func()

# 10. Method overloading - using the same method name but mutlitple paramters can be passed
# method 1
class Arithmetic:
    def multi(self,a,b):
        print(a*b)
    def multi(self,a,b,c):
        print(a*b*c)
obj = Arithmetic()
obj.multi(2,89,899)

# method 2
class Arithmetic:
    def addition(self,*no):
        print(sum(no))
obj = Arithmetic()
obj.addition(45,6898,4988,568)

# 11.method overriding - a child class uses the parent class and its method
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
car = Car()
car.start()

# 12.abstraction - hiding implementation details and showing the essential features
from abc import ABC, abstractmethod
class Company:
    @abstractmethod
    def phase(self):
        pass
class Owner(Company):
    def phase(self):
        print("objective is defined")
class Manager(Company):
    def phase(self):
        print("manages the task")
m = Owner()
n = Manager()
m.phase()
n.phase()

# 13. static method - doesn't require creation of objects
class Student:
    @staticmethod
    def function(a,b,c):
        return a*b*c
print(Student.function(45,629,15200))

# 14. class method - works with the class itself rather than the object
class gadgets:
    @classmethod
    mobile = "android"
    def func(cls,name):
        cls.mobile = name
gadgets.func("apple")
print(gadgets.mobile)

# instance method - uses self, requires object
# class method - uses cls, requires only class
# static method - no use of class/self

'''
15. dunder methods - are double underscores that uses underscore before and after a varaible, it allows to perform special operations in python
__int__ - called when object is initalized
__str__ - Controls what is displayed when you use print(object)
__len__ - Allows an object to work with len().
__add__ - Controls what happens when + is used between objects.
'''