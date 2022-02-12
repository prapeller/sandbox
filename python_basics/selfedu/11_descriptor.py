class CoordDescriptor():
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3D():
    x = CoordDescriptor()
    y = CoordDescriptor()
    z = CoordDescriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

point = Point3D(1, 2, 3)
print(point.__dict__)