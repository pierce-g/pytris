import curses
from curses import wrapper
from Grid import Grid

inputMap = {
    '258': "down_arrow",
    '259': "up_arrow",
    '260': "left_arrow",
    '261': "right_arrow"
}

num_rows = 20
num_cols = 10

def main(stdscr, game_win, game_grid):
    player_input = 0
    while True:
        stdscr.clear()
        stdscr.refresh()

        #display
        for i in range(len(game_grid.grid_spaces)):
            game_win.addstr(i+1, 1, game_grid.row_as_string(i))
        game_win.box()
        game_win.refresh()

        player_input = str(stdscr.getch())
        if player_input in inputMap.keys():
            player_input = inputMap[player_input]

        


def createWin(width, height, x, y):
    game_win = curses.newwin(height+2,width+2,y,x)
    game_win.clear()
    game_win.refresh()

    return game_win

def start(stdscr):
    game_grid = game_grid = Grid(num_cols,num_rows)
    game_win = game_win = createWin(num_cols,num_rows,0,0)
    main(stdscr, game_win, game_grid)


wrapper(start)

