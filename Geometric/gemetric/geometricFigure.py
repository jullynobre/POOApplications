from abc import abstractmethod
import math


class GeometricFigure(object):
    def __init__(self, sides):
        self.sides = sides

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def angles(self):
        pass

    @property
    def meter(self):
        meter = 0
        for i in self.sides:
            meter += i
        return meter


class RegularPolygon(GeometricFigure):
    def __init__(self, side, number_sides):
        self.side = side
        self.number_sides = number_sides
        sides = []
        for i in range(number_sides):
            sides.append(side)
        super(RegularPolygon, self).__init__(sides)

    @property
    def area(self):
        return (self.number_sides*math.pow(self.side, 2))/(4*math.tan(180/self.number_sides*0.0174533))

    @property
    def angles(self):
        angles = []
        for i in range(self.number_sides):
            angles.append((self.number_sides-2)*180/self.number_sides)
        return angles


class Triangle(GeometricFigure):
    def __init__(self, sides):
        super(Triangle, self).__init__(sides)

    @property
    def area(self):
        semi_meter = (self.sides[0]+self.sides[1]+self.sides[2])/2
        return math.sqrt(semi_meter *
                         (semi_meter - self.sides[0])*(semi_meter - self.sides[1])*(semi_meter - self.sides[2]))

    @property
    def angles(self):
        angles = [0, 0, 0]
        cos_s0s1 = (math.pow(self.sides[0], 2) + math.pow(self.sides[1], 2) - math.pow(self.sides[2], 2)) / \
                   (2*self.sides[0]*self.sides[1])
        cos_s1s2 = (math.pow(self.sides[1], 2) + math.pow(self.sides[2], 2) - math.pow(self.sides[0], 2)) / \
                   (2 * self.sides[1] * self.sides[2])
        cos_s0s2 = (math.pow(self.sides[0], 2) + math.pow(self.sides[2], 2) - math.pow(self.sides[1], 2)) / \
                   (2*self.sides[0]*self.sides[2])

        angles[0] = math.acos(cos_s0s1)*57.2958
        angles[1] = math.acos(cos_s1s2)*57.2958
        angles[2] = math.acos(cos_s0s2)*57.2958

        return angles

    def existing_triangle(self):
        if self.sides[0] > self.sides[1] + self.sides[2] or self.sides[0] < module(self.sides[1] - self.sides[2]):
            return False
        if self.sides[1] > self.sides[0] + self.sides[2] or self.sides[1] < module(self.sides[0] - self.sides[2]):
            return False
        if self.sides[2] > self.sides[1] + self.sides[0] or self.sides[2] < module(self.sides[1] - self.sides[0]):
            return False
        return True

    @staticmethod
    def module(value):
        return value * -1 if value < 0 else value

#   1-equilateral 2-isosceles 3-scalene
    @property
    def type(self):
        if self.sides[0] == self.sides[1] == self.sides[2]:
            return 1
        elif self.sides[0] == self.sides[1] | self.sides[0] == self.sides[2] | self.sides[1] == self.sides[2]:
            return 2
        else:
            return 3


class Quadrilateral(RegularPolygon):
    def __init__(self, side):
        super(Quadrilateral, self).__init__(side, 4)


class Square(GeometricFigure):
    def __init__(self, side_b, side_h):
        super(Square, self).__init__([side_b, side_h, side_b, side_h])

    @property
    def angles(self):
        return [90, 90, 90, 90]

    @property
    def area(self):
        return self.sides[0]*self.sides[2]


class Trapeze(GeometricFigure):
    def __init__(self, larger_base, minor_base, height):
        self.height = height
        side = math.sqrt(math.pow((larger_base-minor_base)/2, 2) + math.pow(height, 2))
        super(Trapeze, self).__init__([larger_base, minor_base, side, side])

    @property
    def angles(self):
        cos_larger_base = self.height/self.sides[2]
        a_larger_base = math.acos(cos_larger_base)*57.2958
        a_minor_base = (360 - 2*a_larger_base)/2
        return [a_larger_base, a_larger_base, a_minor_base, a_minor_base]

    @property
    def area(self):
        return (self.sides[0] + self.sides[1])*self.height/2
