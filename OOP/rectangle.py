class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def area(self):
        return round(self.length*self.width,4)

    def perimeter(self):
        return round(2*self.length+2*self.width,4)

if __name__ == '__main__':
    rectangle = Rectangle(float(input('rectangle length [cm] = ')),float(input('rectangle width [cm] = ')))
    print(f"area = {rectangle.area()} [cm*cm]\nperimeter = {rectangle.perimeter()} [cm]")
