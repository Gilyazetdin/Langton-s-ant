class Cell:
    x : int = None
    y : int = None
    size : int = None
    color : str = None

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

class Map:
    height : int = None
    width : int = None
    get: list = None

    def __init__(self, height, width, size, color='white'):
        self.height = height
        self.width = width
        self.get = [[] for i in range(height)]
        for y in range(height):
            for x in range(width):
                self.get[y].append(Cell(x, y, size, color))

def directionFromAngle(angle): # Function returns (x, y)
    if angle == 0:
        return (0, 1)
    elif angle == 90:
        return (1, 0)
    elif angle == 180:
        return (0, -1)
    elif angle == 270:
        return (-1, 0)
    else:
        return None


class Ant(Cell):
    direction : tuple = None
    angle : int = None
    field : Map = None
    left_color : str = None
    right_color : str = None

    def __init__(self, x, y, size, angle, field, color='green', left_color='black', right_color='white'):
        Cell.__init__(self, x, y, size, right_color)
        self.angle = angle
        self.direction = directionFromAngle(self.angle)
        self.field = field
        self.left_color = left_color
        self.right_color = right_color

    def next(self):
        if self.field.get[self.y][self.x].color == self.right_color:
            self.angle = 0 if self.angle + 90 == 360 else self.angle + 90 # Because angle must be 0 not 0
            self.field.get[self.y][self.x].color = self.left_color
        elif self.field.get[self.y][self.x].color == self.left_color:
            self.angle = 0 if self.angle - 90 == -90 else self.angle - 90 
            self.field.get[self.y][self.x].color = self.right_color
        self.direction = directionFromAngle(self.angle)
        self.x += self.direction[0]
        if self.x == self.field.width:
            self.x = 0
        self.y += self.direction[1]
        if self.y == self.field.height:
            self.y = 0
        

    
            

