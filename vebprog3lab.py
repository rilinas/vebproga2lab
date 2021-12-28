import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        result = (math.pi*(math.pow(self.radius, 3))*4)/3
        return result

    def get_square(self):
        result = 4*math.pi*(math.pow(self.radius, 2))
        return result
    
    def get_radius(self):
        return self.radius

    def get_center(self):
        result = (self.x, self.y, self.z)
        return result

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def is_point_inside(self, x2, y2, z2):
        is_true = pow((x2-self.x),2) + pow((y2-self.y),2) + pow((z2-self.z),2) < pow((self.radius),2)
        return is_true

s = Sphere(3, 0, 0, 0)
print('Радиус и координаты сферы')
print(s.get_radius())
print(s.get_center())
print('Объем и площадь поверхности сферы')
print(s.get_volume())
print(s.get_square())

print('Находится ли точка (1, 1, 0) внутри сферы')
print(s.is_point_inside(1, 1, 0))
print('Находится ли точка (4, 5, 10) внутри сферы')
print(s.is_point_inside(4, 5, 10))

s.set_radius(4)
s.set_center(2, 2, 2)
print('Радиус и координаты сферы после изменения')
print(s.get_radius())
print(s.get_center())

s2 = Sphere()
print('Радиус и координаты сферы, созданной без аргументов')
print(s2.get_radius())
print(s2.get_center())
print('Объем и площадь поверхности сферы, созданной без аргументов')
print(s2.get_volume())
print(s2.get_square())
