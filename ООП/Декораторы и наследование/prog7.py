class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return self.x, self.y, self.z


class Block(BaseObject):
    def shatter(self):
        super.__init__(None, None, None)


class Entity(BaseObject):
    def move(self, x, y ,z):
        super.__init__(x, y, z)


class Thing(BaseObject):
    pass
