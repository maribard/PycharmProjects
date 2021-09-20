'''
import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

    def slope(self):
       return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
'''


'''
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius**2 * self.height

    def surface_area(self):
        return 3.14 * self.radius*2 * self.height + 3.14 * self.radius**2 * 2



c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())'''



class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, draw):
        if draw > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= draw

    def __str__(self):
        return f"Account owner:   {self.owner} \nAccount balance: {self.balance}"




acct1 = Account('Jose',100)
print(acct1)

print(acct1.owner)


acct1.deposit(50)
acct1.withdraw(75)


acct1.withdraw(500)