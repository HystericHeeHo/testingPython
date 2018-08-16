class hexagon():
    def __init__(self, s):
        self.side = float(s)
    def calculate_perimeter(self):
        area = ((3 ** 0)/2) * (self.side**2.0)   
        return area
hex1 = hexagon(5)
print(hex1.calculate_perimeter())        