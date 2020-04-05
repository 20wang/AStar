class Space:
    x = 0
    y = 0
    parentX = 0
    parentY = 0
    score = 0

    def __init__(self, x, y, parent, g, h, elev):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = g
        self.h = h
        self.elev = elev

    def __eq__(self, obj):
        return isinstance(obj, Space) and obj.x == self.x and obj.y == self.y

    def setNewParent(self, parent):
        self.parent = parent
