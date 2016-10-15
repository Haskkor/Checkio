##"Animals and plants can reproduce themselves, but it was only recently shown that machines can be made which also reproduce themselves……. Other kinds of self-reproducing machines will be described, and one simple mechanical model, with no electrical or magnetic complications, will be there in working order for the audience to inspect and operate."
##-- Edward Forrest Moore
##In cellular automata, the Moore neighborhood comprises the eight cells surrounding a central cell on a two-dimensional square lattice. The neighborhood is named after Edward F. Moore, a pioneer of cellular automata theory. Many board games are played with a rectangular grid with squares as cells. For some games, it is important to know about the conditions of neighbouring cells for chip (figure, draught etc) placement and strategy.
##
##You are given a state for a rectangular board game grid with chips in a binary matrix, where 1 is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in the form of row and column numbers (starting from 0). You should determine how many chips are close to this cell. Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent.
##
##example
##
##For the given examples (see the schema) there is the same grid:
##
##((1, 0, 0, 1, 0),
## (0, 1, 0, 0, 0),
## (0, 0, 1, 0, 1),
## (1, 0, 0, 0, 0),
## (0, 0, 1, 0, 0),)
##
##For the first example coordinates of the cell is (1, 2) and as we can see from the schema this cell has 3 neighbour chips. For the second example coordinates is (0, 0) and this cell contains a chip, but we count only neighbours and the answer is 1.
##
##Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.
##
##Output: How many neighbouring cells have chips as an integer.
##
##Example:
##
##count_neighbours(((1, 0, 0, 1, 0),
##                  (0, 1, 0, 0, 0),
##                  (0, 0, 1, 0, 1),
##                  (1, 0, 0, 0, 0),
##                  (0, 0, 1, 0, 0),), 1, 2) == 3
##count_neighbours(((1, 0, 0, 1, 0),
##                  (0, 1, 0, 0, 0),
##                  (0, 0, 1, 0, 1),
##                  (1, 0, 0, 0, 0),
##                  (0, 0, 1, 0, 0),), 0, 0) == 1
##
##How it is used: As we mentioned in the beginning, this idea can be useful for developing board game algorithms. In addition, the same principles it can be useful for navigational software, or geographical surveying software.
##
##Precondition:
##3 ≤ len(grid) ≤ 10
##all(len(grid[0]) == len(row) for row in grid)

def count_neighbours(grid, row, col):
    count = 0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i])) and (row != i or col != j) and grid[i][j] == 1:
                count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
