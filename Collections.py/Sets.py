# creation of sets
s = {1,2,3,4}
print(type(s))

# set - removes duplicate values
s = [1,2,31,22,1,22,1,245,1,63]
print(set(s))

# set operations
s1 = {23,11,2341,12,56}
s2 = {23,11,2341,56}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1^s2)
print(s1.issubset(s2))
print(s2.issuperset(s2))
print(s1.isdisjoint(s2))

# set methods
s = s = {1,2,3,4}
print(len(s))  # returns the length of the set
s.add(500) # adds element at the last of  a set
s.update([7,8,9,10000]) # adds multiple values to set
s.remove(3) # removes a element from the set
s.discard(1) # delete the value
result = s.pop() # deletes the element and gives the index value of that
print(result)
s.clear() # clears the entire set
print(s)
# frozen set method - the size of the set is f9xed
