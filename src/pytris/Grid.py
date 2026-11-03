from GridSpace import GridSpace
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_spaces = self.create_grid()

    def create_grid(self):
        #Add GridSpace object to grid_spaces for every space
        grid = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                gs = GridSpace(c,r)
                row.append(gs)
            grid.append(row)
        return grid

    def at_position(self,x,y):
        return self.grid_spaces[y][x]

    def row_as_string(self, row):
        str_row = ""
        for i in self.grid_spaces[row]:
            str_row += i.display

        return str_row
            