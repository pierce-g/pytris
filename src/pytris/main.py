import curses
from curses import wrapper
from Grid import Grid

num_rows = 20
num_cols = 10


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()

    #create window and game grid
    game_win = createWin(num_cols,num_rows,0,0)
    game_grid = Grid(num_cols,num_rows)

    #display
    for i in range(len(game_grid.grid_spaces)):
        game_win.addstr(i+1, 1, game_grid.row_as_string(i))
    game_win.box()
    game_win.refresh()

    stdscr.getch()

def createWin(width, height, x, y):
    game_win = curses.newwin(height+2,width+2,y,x)
    game_win.clear()
    game_win.refresh()

    return game_win




wrapper(main)