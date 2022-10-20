import numpy as np
import time
from datetime import datetime, timedelta

n = 200
grid = np.random.randint(2, size=[n,n])



def count_live_neighbors(grid, pos):
    """ Check for 8 possible neighbors. """

    count = 0

    # Pad the grid to avoid index error.
    grid = np.pad(grid,1)

    # Mind the pad. 
    x = pos[1]+1
    y = pos[0]+1

    # Check for top three cells.
    count += grid[y-1,x-1]
    count += grid[y-1,x]
    count += grid[y-1,x+1]

    # Left and right of the cell.
    count += grid[y,x-1]
    count += grid[y,x+1]

    # Bottom three of the cell.
    count += grid[y+1,x-1]
    count += grid[y+1,x]
    count += grid[y+1,x+1]

    return count


def check_cell(grid, pos):
    """ Apply all four Conway rules to the given cell. """
    
    # First, lets count number of live neighbors.
    live_neighbors = count_live_neighbors(grid, pos)
    status = 0
    live_cell = grid[pos[0], pos[1]]
    # Any live cell with fewer than two live neighbors dies, as of under population.
    if live_cell and live_neighbors < 2:
        status = 0
    
    # Any live cell with two or three live neighbors lives on to the next generation.
    if  live_cell and live_neighbors in [2, 3]:
        status = 1

    # Any live cell with more than three live neighbors dies, as if by overpopulation.
    if live_cell and live_neighbors > 3:
        status = 0
    
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    if not live_cell and live_neighbors == 3:
        status = 1

    return status


def print_ascii(grid):
    
    graph = ""
    for iy, ix in np.ndindex(grid.shape):
        max_x = grid.shape[1]-1

        if grid[iy,ix]:
            graph+=u"\u2588"u"\u2588"
        else:
            graph+="  "

        if ix == max_x:
            graph+="\n"

    print(graph)

test_grid = np.zeros([n,n])
test_grid[0,0] = 1
test_grid[0,-1] = 1
test_grid[-1,0] = 1
test_grid[-1,-1] = 1
print_ascii(test_grid)

time.sleep(3)
while True:

    t = datetime.now()
    new_grid = np.zeros(grid.shape)
    for iy, ix in np.ndindex(grid.shape):
        new_status = check_cell(grid, [iy, ix])

        new_grid[iy, ix] = new_status

    grid = new_grid
    print("td1" ,datetime.now() - t)
    t = datetime.now()
    print_ascii(grid)
    print("td2" ,datetime.now()- t)

    