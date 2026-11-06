'''example 1:
class car with the following attributes and to print them
brand = Toyota
colour = Black
year = 2024'''

class car:
    brand = "Toyota"
    colour = "Black"
    year = 2024

obj = car()
print(obj.brand)
print(obj.colour)
print(obj.year)

'''example 2:
Create a class called Mobile with:
- brand
- model
- price
Create two objects and assign different values to them.
'''

class Mobile:
    brand = "samsung"
    model = "s28"
    price = 96000

obj1 = Mobile()
obj2 = Mobile()

obj1.brand = "apple"
obj1.model = "x21"
obj1.price = 100000

obj2.brand = "poco"
obj2.model = "M3"
obj2.price = 20000

print(obj1.brand,obj1.model,obj1.price)
print(obj2.brand,obj2.model,obj2.price)

'''example 3:
Create a class called Employee with:
- name
- employee_id
- salary
Create three objects and display their details.'''

class Employee:
    name = "incomplete"
    id = 0
    salary = 0

e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.name = "lily"
e1.id = 1
e1.salary = 500

e2.name = "lulu"
e2.id = 2
e2.salary = 1000

e3.name = "lupin"
e3.id = 3
e3.salary = 600

print(e1.name,e1.id,e1.salary)
print(e2.name,e2.id,e2.salary)
print(e3.name,e3.id,e3.salary)

'''example 4 :
Create a class called Calculator with two methods:
- add()
- multiply()
Each method should perform its respective operation and display the result.'''

class Calculator:
    num1 = 10
    num2 = 20
    def add(self):
        sum = self.num1 + self.num2
        print("added value:",sum)
    def multiply(self):
        multi = self.num1 * self.num2
        print("multiplied value:",multi)

obj = Calculator()
obj.add()
obj.multiply()

'''example 5:
Create a class called BankAccount.

Requirements:
- Account holder name
- Account balance
- deposit() method
- withdraw() method
- display_balance() method
Create two bank account objects and perform different transactions.
'''

class BankAccount:
    acc_name = "fill"
    balance = 0
    def deposit(self):
        x = int(input("Enter amount"))
        name = self.acc_name
        self.balance+=x
        print("money deposited")
    def withdraw(self):
        n = int(input("Enter amount:"))
        balance = self.balance
        if n>balance:
            print("insufficient amount")
        else:
            self.balance = balance - n
            print("money withdrawn")
    def display_balance(self):
        print("balance:", self.balance)

customer1 = BankAccount()
customer1.acc_name = "asha"
customer1.balance = 500000

customer2 = BankAccount()
customer2.acc_name = "billy"
customer2.balance = 600000

customer1.deposit()
customer1.withdraw()
customer1.display_balance()

customer2.deposit()
customer2.withdraw()
customer2.display_balance()

