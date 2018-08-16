class triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.s = (side1 + side2 + side3) / 2
    def calculate_area(self):
        area = (self.s * (self.s - self.side1) * (self.s - self.side2) * (self.s - self.side3)) ** 0.5
        return area
tri1 = triangle(3,4,4)
print(tri1.calculate_area())
