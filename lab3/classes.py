# Object-Oriented Programming


class String: # blue-print
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("String: ")

    def printString(self):
        print(self.string.upper())

# okay = String()

# okay.getString()

# okay.printString()

class Shape:
    def __init__(self):
        self.area = 0
    
    def printArea(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length ** 2
    def printArea(self):
        print(self.area)

# shape = Shape()
# shape.printArea()

# square = Square(5)
# square.printArea()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
    def printArea(self):
        print(self.area)

# rectangle = Rectangle(5, 10)
# rectangle.printArea()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    
    def move(self, mvd_x, mvd_y):
        self.x = mvd_x
        self.y = mvd_y
    def dist(self, other_point):
        print(self.x - other_point.x, self.y - other_point.y)

# point = Point(0, 0)
# point.show()
# point.move(5,5)
# point.show()

# point2 = Point(9,9)

# point.dist(point2)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} : Deposited {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} : Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} : Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} : Insufficient funds or invalid amount.")
            

# client1 = Account("Gi-Hun", 45600000)

# client1.withdraw(45600000)

# account = Account("Sae-byeok", 100.0)
# account.deposit(50)
# account.withdraw(30)
# account.withdraw(150)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

filter_primes = lambda numbers: list(filter(lambda x: is_prime(x), numbers))

# print(filter_primes([1,2,3,4,5,6,7,8,9,10]))