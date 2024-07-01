import numpy as np

class Point2D:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
    
    def euclidean_distance(self, point):
        distance = np.sqrt((point.x-self.x)**2 + (point.y-self.y)**2)
        return round(distance,4)

    def __str__(self):
        return f"({self.x},{self.y})"


if __name__ == '__main__':

    p1 = Point2D((5,5))
    p2 = Point2D((1,-4))
    print(p1.euclidean_distance(p2))
