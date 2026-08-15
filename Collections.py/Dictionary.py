# creating dictionary - contains (key, value) pairs, where the keys must be unique
d = {10:'apple',20:'banana',30:'mangoes'}

# mutability - dictinaries values can be changed
d[10] = "oranges"  
print(d)

# length of a dictionary
print(len(d))

# checking existence of a value 
d = {10:'apple',20:'banana',30:'mangoes'}
if 10 in d:
    print("exists")

if 'apple' in d.values():
    print("yes")
    
# dictionary methods

# accesing a value in dictionary
# method 1
print(d[20])
# method 2
print(d.get(30))

# adding values to a dictionary
d[40] = "kiwi"
print(d)

# updating values in a dictionary
# method 1
d[20] = "lichi"
print(d)

# method 2
d.update({50:'gauva'})
print(d)

# removing values from a dictionary
# method 1 
result = d.pop(50) # returns the deleted value
print(result)
print(d)

# method 2 
d.popitem() # deletes the last key value pair
print(d)

# method 3
del d[30]
print(d)

# method 4
d.clear() # deletes the entire dictionary and returns only a empty dictionary
print(d)

# key - returns all the keys present in the dictionary in the form of a list
print(d.keys())

# values - returns all the values present in form of list
print(d.values())

# items - retuns key - value pairs in form of tuples inside a list
print(d.items())

# setdefault - returns the value if key exists, if not exists it creates it
d.setdefault(40,'jello')
print(d)

# creating a copy of dictionary
new = d.copy()
print(new)

# fromkeys - creating a dictionary from keys
# method 1
k = [23,45,2,53,5]
new_d = d.fromkeys(k)
print(new_d)

# method 2 
k = [23,45,2,53,5]
new_d = d.fromkeys(k,'nill')
print(new_d)

# looping in dicitonary
student = {
    "name": "lisa",
    "age": 20,
    "course": "CSE"}
# method 1
for key in student.keys():
    print(key)

# method 2
for value in student.values():
    print(value)

# method 3
for key,value in d.items():
    print(key,value)

# nested dicitonary
students = {
    "student1": {
        "name": "max",
        "age": 20
    },
    "student2": {
        "name": "lucy",
        "age": 21
    }
}

# zip - creating a dictionary 
k = [23,45,2,53,5]
v = ['its','a','bright','day',"isn't"]
modified = dict(zip(k,v))
print(modified)