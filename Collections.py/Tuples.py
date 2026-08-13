# creating tuples
t = (0,2,"hello",['dog',89])

# creating multiple tuples
t1 = ("good","brilliant","smart")
t2 = (32,50,114,90)
result = tuple((zip(t1,t2)))
print(result)

# convert any type of datatype into tuple
l=[90,'hey',734]
print(tuple(l))

# concatenation of tuples
t1 = ("good","brilliant","smart")
t2 = (32,50,114,90)
result = t1+t2
print(result)

# replication of tuples
t = ("good","brilliant","smart")
print(t*2)

# indexing in tuples
print(t[1])
print(t[-2])

# slicing in tuples
print(t[::-1])
print(t[0:2])

# tuples are immutable - you cannot change the values
#t[1] = "marvellous"  not possible

# tuple methods
print(t.count("good")) # it returns the count of character in a tuple
print(t.index("smart")) # returns the index postion of the character

# tuple functions
l = (2,34,654,90,45)
print(len(l)) # gives length of a tuple
print(sum(l)) # gives the sum of values in tuple
print(max(l)) # gives the maximum value in tuple
print(min(l)) # gives the minimum value in tuple
ans = sorted(l) # returns a sorted list
print(ans)
answer = reversed(l) # reversed tuple
print(answer)
print(any(l)) # returns true if any element is true
print(all(l)) # returns true if all elements are true

# enumerate - it is a type of iterator which returns both index and value
for index,value in enumerate(t):
    print(index,value)

# for loop iteration in tuple
t = (32,50,114,90)
for i in t:
    print(i/2)

# while loop iteration in tuple
t = (32,50,114,90)
i=0
while i<len(t):
    print(t[i])
    i+=1

# nested tuples
t = (
    (32,50,114,90),
    (213,65,89,35),
    (56,87,658))
print(t[0][2])
print(t[2][2])

# map - applying a function to each and every element inside a tuple
t = (32,50,114,90)
result = tuple(map(lambda x : x+10, t))
print(result)

# filter - extracting elements from a tuple based on the condition
t = (32,50,114,90)
result = tuple(map(lambda x : x%10 ==0, t))
print(result)

# tuple packing
t = 'he','is',1,30,'smart'
print(t)
# tuple unpacking
t = (32,50,114,90)
one,two,three,four = t
print(one)
print(two)
print(three)
print(four)

# checking existence of a character
t = (32,50,114,90)
if 50 in t:
    print("exits")

a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)
print(a is b)

print(id(t)) # it returns the memory reference of the object
print(bool(t)) # returns the boolean value of the characters

# tupple aliasing
t = ('stone','paper','scissor') 
m = t
print (m)

# deleting values of a tuple
n = ('its',50,'raining')
del n


