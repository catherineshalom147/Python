String = "python is a fun language"
name = 'Sarah'

# conversion to a string
num = 10
print(str(num))

# string indexing
print(String[0])
print(name[2])
print(name[-3])

# string slicing - parameters [start:stop:step]
print(String[:15:2])
print(name[-1:-4:-1])

# string methods
print(name.upper()) # upper method
print(name.lower()) # lower method
print(String.capitalize()) # captialize the first word
print(String.title()) # convert the string into title format
print(String.strip()) # removes the leading and trailing spaces
print(String.lstrip()) # removes leading spaces
print(String.rstrip()) # removes trailing spaces
print(name.replace("Sarah",'Sam')) # replacing a string
print(String.split(" ")) # dividing a string based on a character
print(name.isupper()) # checks if the string is in upper case
print(name.islower()) # checks if the string is in lower case
print(String.isdigit()) # checks if the string is numbers
print(String.isalpha()) # checks if the string is alphabets
print(name.startswith("S")) # checks if a string starts like the character
print(String.endswith('language')) # checks if a string's character ends like that
print(String.find("fun")) # returns the index of a substring
print(name.count("a")) # returns the count of a character
print(String.isalnum()) # checks if the string is a combination of alphabets and numbers
new = " ". join(String)
print(new) # creating a new string based on a character

# string formats
# method 1
name = "dog"
age = 8
price = 1245.89
print("this a  name : %s of age : %d with a price tag of : %f " %(name,age,price))

# method 2
print("this is a {} of age {} with price tag of {}".format(name,age,price))

# method 3
print(f"this is a {name} of age {age} with cost of {price}")

# escape sequences
print("first\nline") # new line
print("second\tline") # tab
print("third\\line") # backslash
print("fourth_line\'s") # single quote
print("fifth \"line\" ") # double quotes

# encoding - converting string to bytes
data = "hello world"
result = data.encode('utf-8')
print(type(result))

# decoding - converting byte code into string
data = b'Hello, World! \xf0\x9f\x8c\x8d'
result = data.decode('utf-8')
print(type(result))
