class apple():
    #Weight in oz, length/width in cm
    def __init__(self, c, wgt, l, w, h):
        self.color = c
        self.weight = wgt
        self.length = l
        self.width = w
        self.height = h 
        print('Created')
    def area(self):
        return self.length * self.width * self.height

apl1 = apple('Crimson', 0.3, 2.2, 1.3, 3.5)
