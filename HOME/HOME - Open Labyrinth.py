##The labyrinth has no walls, but bushes surround the path on each side. If a players move into a bush, they lose. The labyrinth is presented as a matrix (a list of lists): 1 is a bush and 0 is part of the path. The labyrinth's size is 12 x 12 and the outer cells are also bushes. Players start at cell (1,1). The exit is at cell (10,10). You need to find a route through the labyrinth. Players can move in only four directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]), West (left [0, -1]). The route is described as a string consisting of different characters: "S"=South, "N"=North, "E"=East, and "W"=West.
##
##open-labyrinth
##
##Input: A labyrinth map as a list of lists with 1 and 0.
##
##Output: The route as a string that contains "W", "E", "N" and "S".
##
##Example:
##
##checkio([
##    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
##    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
##    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
##    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
##    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
##    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
##    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
##    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
##    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
##    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
##    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
##
##How it is used: This is a classical problem for path-finding in graphs -- Yes, the maze can be represented as a graph. It can be used in navigation software for a to b navigation and computer games for artificial intelligence. You can find your way anywhere you wish. Just divide a map into square cells and mark up the "bad" cells.
##
##Precondition: Outer cells are pits.
##len(labyrinth) == 12
##all(len(row) == 12 for row in labyrinth)

import copy
import random

def find_free(maze,line,col):
    """ Find free squares around the acutal position. """
    free = []
    if maze[line-1][col] == 0:free.append([line-1,col])
    if maze[line+1][col] == 0:free.append([line+1,col])
    if maze[line][col-1] == 0:free.append([line,col-1])
    if maze[line][col+1] == 0:free.append([line,col+1])
    return free
    
def choose_way(free,line,col,old_line,old_col,results,walked_path):
    """ Choose a way to go between the free squares. """
    temp_free = []
    free_not_walked = []
    # Si il n'y a qu'un choix
    if len(results) < 1 or len(free) < 2:
        return free[0][0],free[0][1],line,col
    else:
        # Enlève la case précédente du choix ainsi que les cases déjà
        # parcourues puis en choisi une au hasard
        for case in free:
            if case[0] != old_line or case[1] != old_col:
                temp_free.append(case)
        for case_free in temp_free:
            if walked_path[case_free[0]][case_free[1]] == 0:
                free_not_walked.append(case_free)
        if len(free_not_walked) > 0:
            temp = random.choice(free_not_walked)
        else:
            temp = random.choice(temp_free)
        return temp[0],temp[1],line,col
    
def fill_result(line,col,old_line,old_col):
    """ Fill the result string. """
    if line > old_line:return "S"
    elif line < old_line:return "N"
    elif col < old_col:return "W"
    elif col > old_col:return "E"

def checkio(maze_map):
    walked_path = copy.deepcopy(maze_map)
    result = ""
    line,col,old_line,old_col = 1,1,1,1
    while not (line == 10 and col == 10):
        walked_path[line][col] = 2
        free_squares = find_free(maze_map,line,col)
        line,col,old_line,old_col = choose_way(free_squares,line,col,old_line,old_col,result,walked_path)
        result += fill_result(line,col,old_line,old_col)
    return result

if __name__ == '__main__':
    #This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        #copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False

    # These assert are using only for self-testing as examples.
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],    
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
    print("The local tests are done.")
