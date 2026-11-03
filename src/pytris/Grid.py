from GridSpace import GridSpace
from Piece import Piece
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

    def clear_screen(self):
        for r in self.grid_spaces:
            for c in r:
                c.display = " "

    def draw_piece(self, piece):
            row = 0
            col = 0
            for i in piece.shape:
                if i == '.':
                    self.grid_spaces[row+piece.y][col+piece.x].display = '.'
                    col += 1
                elif i == '|':
                    row +=1
                    col = 0