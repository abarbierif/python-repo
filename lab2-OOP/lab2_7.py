import numpy as np

class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def area(self):
        return round(self.length*self.width,4)

    def perimeter(self):
        return round(2*self.length+2*self.width,4)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(np.pi*self.radius**2,4)

    def perimeter(self):
        return round(2*np.pi*self.radius,4)

N = int(input('N = '))
l = []
for _ in range(N):
    if np.random.randint(0,2):
        l.append(Rectangle(np.random.uniform(0.0,100.0),np.random.uniform(0.0,100.0)))
    else:
        l.append(Circle(np.random.uniform(0.0,100.0)))


for _ in l:
    if isinstance(_,Rectangle):
        print(f"Rectangle area = {_.area()} [cm*cm]")
    else:
        print(f"Circle area = {_.area()} [cm*cm]")

l_sorted = sorted(l, key = lambda _:_.area(), reverse = False)
print('\n')
for _ in l_sorted:
    if isinstance(_,Rectangle):
        print(f"Rectangle area = {_.area()} [cm*cm]")
    else:
        print(f"Circle area = {_.area()} [cm*cm]")
 

