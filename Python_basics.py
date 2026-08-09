# printing a simple statement in python
print("Welcome to python tutorial")

# # ~ represents single line comment
# ''' ~ represents multi line comments '''

# Varaibles (dynamic type - datatype of variable can be changed) 
# defining a variable
x = 10
name = "cat"

# Data types 
a = 10
print(type(a))
b = 12.4
print(type(b))
c = 5 + 6j
print(type(c))
d = True
print(type(d))
name = "lily"
print(type(name))
L = ['apple',2,8.9,0]
print(type(L))
Things = ("hello","welcome",23,14)
print(type(Things))
S = {1,23,4,56}
print(type(S))
dictionary = {"alpha":0,"omega":1,"beta":2}
print(type(dictionary))
Result = None
print(type(Result))

# Type conversion - converting one type of data into another form

# implicit type conversion - python automatically converts the datatype
x = 10
y = 20.0
print(x+y)

# Explicit type conversion - we convert the datatype manually
m = "50"
n = int(m)
print(n)

# getting input & output ( input function always return a string )
# method - 1
greet = input("Enter your greeting phrase - ")
roll_no = int(input("Enter your enroll number:"))
print (greet,roll_no)

#method - 2
greet = input("Enter your phrase:")
printf("{greet} It was nice meeting you!")

# Keywords - are reserved by python and have special meaning for it
'''False, None, True, and, as, assert, async, await, break, case, 
class, continue, def, del, elif, else, except, finally, for, from,
global, if, import, in, is, lambda, match, nonlocal, not, or,
pass, raise, return, try, while, with, yield
'''

# Identifiers - are variables
'''
1x = 10 (identifiers should not start with numbers)
hello*world = "YES" (variables should not contain special characters but _ is allowed)
True = "yes" (variables are not keywords)
'''

# Operators - set of symbols on which operations are performed

# 1. Arithmetic operators
u = 10
v = 5
print(u+v) # addition
print(u-v) # subtraction
print(u*v) # multiplication
print(u/v) # division
print(u//v) # floor division
print(u%v) # remainder
print(u**v) # power

# 2. Assignment operators
a = 10
a += 5 
a -= 2
a *= 3
a /= 2
a //= 2
a %= 5
a **= 4

#