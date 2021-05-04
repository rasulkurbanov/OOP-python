class Point3D:
    x = 1
    y = 1


    def setCoordinates(self, a=3, b=5, c=9):
        self.x = a
        self.y = b
        self.z = c


pt = Point3D()
pt.setCoordinates()


class Point:
    def __init__(self, )