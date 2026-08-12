# creation of list
L = ["apple", 23, "bye", 67]

# converting a datatype to list
string = "python"
L = list(string)

# concatenation of list
l1 = [321,54,3456,21]
l2 = [15,5981,4,6563]
result = l1 + l2
print(result)

# replication of list
new_list = ["a","b","c","d"]
print(new_list * 3)

# indexing - accesing individual charcters 
L = ["apple", 23, "banana", 67, "orange"]
print(L[2])
print(L[-2])

# slicing - extracting a part of list (parameters - [start:stop:step])
L = ["apple", 23, "banana", 67, "orange"]
print(L[1:4]) 
print(L[-1:-5])

# Lists are mutable - you can change the values inside a list
L = ["apple", 23, "banana", 67, "orange"]
L[3] = "mango"

# list methods
L = ["apple", 23, "banana", 67, "orange"]
L.append(92) # adds a single value at the end of a list
print(L)
L.extend(["kiwi",45,67]) # adds multiple values at end of a list
print(L)
L.insert(2,"58") # insert value based on the index position
print(L)
L.remove("orange") # removes a value from list
print(L)
L.pop(3) # removes a value based on the index and returns the deleted value
print(L)
L.pop() # no parameter passed, deletes the last parameter
print(L)
L.clear() # deletes entire List and returns empty list
print(L)
n = L.index("kiwi") # returns the index position of a value
print(n)
c = L.count(67) # returns the number of occurences of a value
print(c)
new_L = [23,11,42,0,221]
duplicate = new_L.copy() # a copy of list is returned
print(duplicate)
new_L.sort() # it returns a sorted list in ascending order by default
print(new_L)
new_L.sort(reverse = True)
print(new_L)
new_L.reverse() # returns a reversed list
print(new_L)


# list functions
print(len(new_L)) # returns the length of the list
print(max(new_L)) # returns the maximum value in list
print(min(new_L)) # returns minumum value in list
print(sum(new_L)) # returns the entire added value

# checking if a element exist
a = ["alpha","omega",'beta','gamma']
print("alpha" in a)

# looping in list
a = ["alpha","omega",'beta','gamma']

#method 1
for i in a:
    print(i)

# method 2 
for i in range(len(a)+1,2):
    print(i)

# method 3
c = 0
while c< len(a):
    print(c)
    c+=1

# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix [0])
print(matrix[0][2])

