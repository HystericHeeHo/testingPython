from math import pi

class circle():
    #Weight in oz, length/width in cm
    def __init__(self, r):
        self.radius = r
        print('Created!')
    def get_area(self):
        return pi * self.radius ** 2

cir1 = circle(2)
print(cir1.get_area())