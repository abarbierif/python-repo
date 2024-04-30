class Point2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def euclidean_distance(self, another2Dpoint):
        return round(((another2Dpoint[0]-self.x)**2 + (another2Dpoint[1]-self.y)**2)**(1/2),4)
    
    def __repr__(self):
        return f"({round(self.x,4)}, {round(self.y,4)})"

#p1 = Point2D(12,4)
#another2Dpoint = (67,90)
#print(f"euclidean distance to {another2Dpoint} = {p1.euclidean_distance(another2Dpoint)}")
