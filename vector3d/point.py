from math import sqrt

class Point:
    x = float()
    y = float()
    z = float()

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other_point):
        is_point_bool = isinstance(other_point, Point)
        is_x_eq = self.x == other_point.x
        is_y_eq = self.y == other_point.y
        is_z_eq = self.z == other_point.z
        return(is_point_bool and is_x_eq and is_y_eq and is_z_eq)

    def __ne__(self, other_point):
        is_point_bool = isinstance(other_point, Point)
        is_x_eq = self.x == other_point.x
        is_y_eq = self.y == other_point.y
        is_z_eq = self.z == other_point.z
        if (is_point_bool and is_x_eq and is_y_eq and is_z_eq):
            return(False)
        else:
            return(True)

    def clone(self):
        return(Point(self.x, self.y, self.z))

    def equals(self, other_point):
        return(self == other_point)

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def getZ(self):
        return(self.z)

    def getLocation(self):
        return(Point(self.x, self.y, self.z))

    def getLocationTuple(self):
        return((self.x, self.y, self.z))

    def move(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def setLocation(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def setLocationFromPoint(self, other_point):
        self.x = other_point.x
        self.y = other_point.y
        self.z = other_point.z

    def toString(self):
        return('Point: %(point_x)s, %(point_y)s, %(point_z)s' %{'point_x': self.x, "point_y": self.y, "point_z": self.z})

    def translate(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z

def distance(a, b):
    # print("calculating distance between points: ", a.toString(), b.toString())
    return sqrt((b.x - a.x)^2 + (b.y - a.y)^2 + (b.z - a.z)^2)

def center(a, b):
    return Point((b.x - a.x)/2 + a.x, (b.y - a.y)/2 + a.y, (b.z - a.z)/2 + a.z)
