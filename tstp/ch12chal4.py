class hexagon():
    def __init__(self,a,b,c,d,e,f):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
        self.side5 = e
        self.side6 = f
    def calculate_perimeter(self):
        perimeter = self.side1+self.side2+self.side3+self.side4+self.side5+self.side6
        return perimeter
hex1 = hexagon(5,1,2,4,3,6)
print(hex1.calculate_perimeter())        