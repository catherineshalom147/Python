''' two types of functions
1. built in functions - defined by python already
ex : len, input
2. user defined functions - created by the programmmers'''

# creating a function 
def sum(a,b):
    print (a+b)

# calling a function
def multi(x,y):
    return (x*y) # using return preserves the value, the value is return back to the function
a = 10
b = 5
print(multi(a,b))

# arguments vs parameter
# 1. function with parameter and without argument
def sum(a=3,b=6):
    return("it's",a+b )
print(sum())

# 2. function with argument, with parameter
def greet(s):
    return(s,"added")
s= "hello"
print(greet(s))

# 3. function without parameter and argument
def greet():
    return("good morning")
print(greet())

# types of arguments
# 1. default arguments - values given if not passed as arguments , must be as a end parameter
def student(roll,name,age,dept='cse'):
    print(roll,':',name)
student(101,'Lily',18)

# 2. keyword arguments - arguments passed by mentioning the parameters alongside, ordering doesn't matter
def stud(name,course):
    return(name,course)
print(stud(course = 'Mech',name = 'Max'))

# 3. positional arguments - arguments given based on position
def stud(roll,name,dept):
    return(roll,name,dept)
print(stud(101,'Max',"ECE"))
    
# 4. variable length arguments - names are conventional
# args - when number of postional argument is unkonwn, values returned as tuples
def fruits(*values):
    return(values)
print(fruits('apple','banana','mango'))

# kwargs - used when number of keyword arguments is unknown, values returned as dictionary
def course(**details):
    return(details)
print(course(course_name = 'EEE', course_id = 2201))

# scope of variables
# global - variable defined outside a function but can be used inside a function using global keyword
# local - variable defined inside a function
x = 10 # global
def new(y):
    global x
    return (x + y)
print(x,5)

# recursion function - a function being called inside a function
def fact(n):
    if n == 1:
        return (n)
    else:
        return n * fact(n-1)
print(fact(5))

# Lambda function - used when a small temporary function is required
square = lambda x : x**2
print(square(8))

# Higher order functions - takes another function as argument or returns a function
def func(parameter1,number):
    return (parameter1(number))
answer = func(lambda x : x%2 == 0,34)
print(answer)

# built - in higher order functions
# map - applies a function to all element
l=[2,3,4,5,6]
resultant = list(map(lambda x: x**2,l))
print(resultant)

# filter - it keeps elements which satisfy a condition
l=[2,3,4,5,6,7]
result = list(filter(lambda x : x%2 != 0,l))
print(result)

# sorted 
students = [
    ("John", 80),
    ("Alice", 95),
    ("Alex", 75)
]

students = sorted(students)
# or
students = sorted(students, key=lambda student: student[0])
print(students)