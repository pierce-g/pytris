import curses
from curses import wrapper

num_rows = 20
num_cols = 10


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    game_win = createWin(num_cols,num_rows,0,0)
    
    game_win.refresh()
    stdscr.getch()

def createWin(width, height, x, y):
    game_win = curses.newwin(height,width,y,x)
    game_win.clear()
    return game_win


wrapper(main)