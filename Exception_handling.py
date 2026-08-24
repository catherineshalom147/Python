# exception handling - refers to handling the error that occur when a program is running

# try - the block contains the code with error
try:
   a = 10
   b = 0
   print(a/b)

# except - the block is used to handle the error
try:
   a = 10
   b = 0
   print(a/b)
except:
   print("the input given is wrong")

# you can have multiple except blocks
try:
   a = 10
   b = 0
   print(a/b)
except ArithmeticError:
   print("the input given is wrong")
except ZeroDivisionError:
   print("the value cannot be divided by zero")

# else - the block is executes when there is no error in the code
try:
   a = 10
   b = 2
   result = a/b
except:
   print("the input given is wrong")
else:
   print(result)

# finally - the block executes the code whatever be the case, it is executed always
try:
   a = 10
   b = 0
   print(a/b)
except ZeroDivisionError:
   print("you cannot divide a number by zero")
finally:
   print("the program was executed successfully")

# raise - it is used when you want to create an exception
a = 20
if a % 2 !=0 :
   raise Exception ("the value is wrong")
else:
   print("true")

# raise with try and except
try:
   a = 'age'
   if a != 20:
      raise ValueError("the input passed is incorrect")
except ValueError as e:
   print(e)

# custom exceptions
# method 1
class detailError(Exception):
   print("details entered must be in correct format")

age = 18

try:
   if age< 20:
      raise detailError()
except detailError as d:
    print(d)

# method 2
class InvalidMarksError(Exception):
    pass

try:
    marks = 60
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
except InvalidMarksError as e:
    print(e)


# Assertions - it is used to check whether  a condition is true
marks = 30
assert marks >= 50
print("pass")

# assert can provide messages
marks = 50
assert marks >= 50, "the value provided is not elgible"