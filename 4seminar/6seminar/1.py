from oop import OOP
class Vector(OOP):
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        if isinstance(x, str):
            x, y, z = x.strip('{}').split(',')
            x, y, z = float(x), float(y), float(z)

        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))

        self.x = x
        self.y = y
        self.z = z

    @OOP.method
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    @OOP.method
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    @OOP.method
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Не вектор и не число!")

    @OOP.method
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    @OOP.method
    def __str__(self):
        return f"{{x: {self.x}, y: {self.y}, z: {self.z}}}"

    @OOP.method
    def __repr__(self):
        return self.__str__()

    @OOP.method
    def to_tuple(self):
        return (self.x, self.y, self.z)