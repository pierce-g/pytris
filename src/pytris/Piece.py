class Piece:
    def __init__(self, name, shape, x, y):
        self.name = name
        self.shape = shape
        self.x = x
        self.y = y
        self.active = False
        self.width, self.height = self.get_size()

    def get_size(self):
        w = 0
        width = 0
        h = 1
        for i in self.shape:
            if i == "|":
                h += 1
                if width > w:
                    w = width
                width = 0
            else:
                width += 1
            
        if width > w:
            w = width
        return w, h

    def setActive(self, active):
        self.active = active

    def move(self):
        if self.y < 20 - self.height:
            self.y += 1