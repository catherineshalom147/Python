# if statements - evaluates for a single condition
n = 28
if (n%2 == 0):
    print("True")

# if - else statements - similar to yes or no 
value = 200
if value > 500:
    print("Amount insufficient")
else:
    print("Amount is still left")

# if - elif - else statements - when more than one condition occurs
marks = 50
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# nested if else statements - when we use a condition inside a condition
marks = 50
attendance = 80
if marks >= 50:
    if attendance >= 80:
        print("promoted")
    else:
        print("low attendance")
else:
    print("Depromoted")

# match case statements
'''classes = 4
match classes:
    case 1:
        print("class I")
    case 2:
        print("class II")
    case 3:
        print("class III")
    case 4:
        print("class IV")
    case _:
        print("Invalid")'''

# for loop - to iterate over a sequence
#method 1
n = ['a','b','c']
for i in n:
    print(i)

#method 2
n = 5
for i in range(0,n+1,1): # (start,stop,step)
    print(i)

# while loop - the loop runs as long the condition remains true
n = 2
i = 0
while i<=n:
    print(i*2)
    i=i+1

# break statement - it is used to discontinue a loop
for i in range(0,5,1):
    if i == 2:
        break
    else:
        print(i)

# continue statement - it is used to skip any one iteration of the loop
for i in range(0,5,1):
    if i == 2:
        continue
    else:
        print(i)
    i+=1

# pass statement - are simply empty statement
name = "heycatzz"
if name != " ":
    pass

# nested loop statements - there will be a loop inside a loop
for i in range(0,6,1):
    for j in range(1,i+1,1):
        print(j, end = " ")
    print()