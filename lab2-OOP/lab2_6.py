from lab2_5 import Point2D
import random
import numpy as np

N = int(input('length of Points2D: '))
Points2D = [Point2D(random.uniform(0,20),random.uniform(0,20)) for _ in range(N)]
Points2D_sorted = sorted(Points2D, key = lambda _:_.euclidean_distance((0,0)), reverse = False)

for _ in range(len(Points2D_sorted)):
    if _ == len(Points2D_sorted)-1:
        print(Points2D_sorted[_],'\n')
    else:
        print(Points2D_sorted[_])

#Points2D_euclideandistance = {}
#for _ in Points2D:
#    Points2D_euclideandistance[_] = _.euclidean_distance((0,0))
#
#Points2D_Sorted = [_[0] for _ in sorted(Points2D_euclideandistance.items(), key = lambda _:_[1], reverse = False)]
#
#print(Points2D_Sorted)

class Circle(Point2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(np.pi*self.radius**2,4)

    def perimeter(self):
        return round(2*np.pi*self.radius,4)

    def contains(self, point2D):
        if (point2D.x-0)**2 + (point2D.y-0)**2 <= self.radius**2:
            return 'True'
        else:
            return 'False'


circle = Circle(float(input('radius [cm]: ')))
print(f"circle area = {circle.area()} [cm*cm]")
print(f"circle perimeter = {circle.perimeter()} [cm]")
point2D = Point2D(1,2)
print(f"is {point2D} inside the circle? {circle.contains(point2D)}")

