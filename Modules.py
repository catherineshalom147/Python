# importing a module
# import module_name, Ex : math module
# method 1
import math
n = 5
print(math.sqrt(n))

# method 2
from math import factorial,pi
print(factorial(34))
print(pi)

# method 3 
from math import *
print(sqrt(4))
print(floor(32.21))

# method 4
import math as m
print(m.ceil(6.34))
print(m.floor(24.3))

# built in modules - such as math, statistics, random, numpy,datetime..
import statistics as stat
l=[1,23,42,64,23,5,43,2]
print(stat.mean(l))
print(stat.median(l))

# modules can be created
# create a module named student.py, inside it
def basic_info(roll_no,name,level):
    return(roll_no,":",name,":",level)
def subject_marks(eng,mat,sci,socio):
    return(eng,mat,sci,socio)
def criteria(eng,mat,sci,socio,attendance):
    result = eng+mat+sci+socio
    if result > 50 and attendance > 90:
        return ("pass")
    else:
        return ("fail")
import student as s
print(s.basic_info(101,'isha',2))

# packages - multiple modules stored inside a package