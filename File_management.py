# open (filename, mode)
# create new file
f = open("newfile.txt",'x')
f.close()

# Reading text files
# method 1 - read()
file = open("file.txt",'r')
content = file.read() # reads entire file, input parameters can also be passed from which position to read
print(content)
file.close()

# method 2 - readline() - used to read asingle line from a file
file = open("file.txt",'r')
content = file.readline()
print(content)
file.close()

# method 3 - readlines() - it returns each line in the file in list format
file = open("notes.txt",'r')
content = file.readlines()
print(content)
file.close()

# writing into text files - contents are overwritten
# method 1
f = open('data.txt','w')
f.write("new contents added")
f.close()

# method 2
lines = ["Python\n", "Java\n", "C++\n"]
f = open("data.txt",'w')
f.writelines(lines)
f.close()

# tell () - the function returns the current position of the cursor
file = open("note.txt",'r')
print(file.tell())

# seek () - it keeps the cursor at the desired point ( if parameter = 0 - start position, if parameter = -1 - at end position)
with open("data.txt", "r") as file:
    file.seek(0)

# appending into text files 
f = open("data.txt",'a')
f.write("data to be written is continued")
f.close()

# reading a binary file
with open("image.jpg", "rb") as file:
    data = file.read()

# writing a binary file
data = b"Hello"
with open("data.bin", "wb") as file:
    file.write(data)
print(data)

'''File modes determine what operations can be performed on a file.
"r"	- Read
"w"	- Write / overwrite
"a"	- Append
"x"	- Create a new file
"r+" - Read + Write
"w+" - Write + Read, overwrites
"a+" - Append + Read
"rb" - Read binary
"wb" - Write binary'''

# with open - will allow the function without using close the file at end, it automatically closes
with open("data.txt",'r') as file:
    content = file.read()
print(content)

# reading csv files
import csv
with open("data.csv",'r') as f:
    read = csv.reader(f)
    for i in read:
        print(i)

# writing csv files
import csv

data = [
    ["Name", "Age", "Mark"],
    ["John", 20, 85],
    ["Mary", 21, 90]
]

with open("data.csv",'w',newline="") as file:
    write = csv.writer(file)
    writer.writerows(data)

# reading json files
import json
with open("files.json",'r') as new:
    content = json.load(file)
print(content)

# loads - converts string into python object
import json
data = '{"name": "John", "age": 20}'
result = json.loads(data)
print(result)

# writing json files
import json
student = {
    "name": "John",
    "age": 20,
    "skills": ["Python", "SQL"]
}
with open("file.txt",'w') as file:
    json.dump(student,file,indent= 4)

# dumps - python object into string
import json
data = {
    "name": "John",
    "age": 20
}
result = json.dumps(data)
print(result)

# encoding - converting strings into bytes
text = "Python"
data = text.encode("utf-8")
print(data)

# decoding - converting bytes into strings
data = b"Python"
text = data.decode("utf-8")
print(text)