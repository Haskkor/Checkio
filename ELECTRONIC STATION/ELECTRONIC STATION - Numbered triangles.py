##Our robots like games that require the ability to calculate equations. Mission control recently sent them the new game to occupy their time while flying from one Island to the next. This game is called "Numbered Triangles". Players take 6 chips from the pile, each chip is made of an equilateral triangle with three numbers one on each edge. You can move, rotate and flip the chips so they form a hexagon. The hexagon is only legal if the adjacent edges for each triangle have matching numbers.
##
##The score for a legal hexagon is the sum of the numbers on the outside six edges. The player's goal is to find the highest score that can be achieved with the given six chips.
##
##Each chip is represented as a list with three positive numbers. You should help the robots find the highest score for the given chips and return the score as a number. If you cannot form legal hexagon from the chips, then return a score of 0.
##
##Input: The chip info as a list of lists. Each list contain three integers.
##
##Output: The highest possible score as an integer.
##
##Example:
##
##checkio([[1, 4, 20], [3, 1, 5], [50, 2, 3],
##         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152
##checkio([[1, 10, 2], [2, 20, 3], [3, 30, 4],
##         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210
##checkio([[1, 2, 3], [2, 1, 3], [4, 5, 6],
##         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21
##checkio([[5, 9, 5], [9, 6, 9], [6, 7, 6],
##         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0
##​
##How it is used: This concept is used in optimization systems; you have constraints but you should work to get the most with these constraints. Of course this algorithm can be useful for the realisation of gameplay mechanics.
##
##Precondition:
##len(chips) == 6
##all(all(0 < x < 100 for x in ch) for ch in chips)

from itertools import permutations as perm
import copy
​
def find_link(elem,chips,hexa,hexas):
    if len(hexa) == 6 and hexa[0][0] == hexa[-1][-1] and hexa not in hexas:
        hexas.append(hexa)
    for i,chip in enumerate(chips):
        for perms in perm(chip):
            if elem[2] == perms[0]:
                temp_hexa = copy.deepcopy(hexa) + [perms]
                find_link(perms,chips[:i]+chips[i+1:],temp_hexa,hexas)
​
def checkio(chips):
    if all([elem == chips[0][0] for chip in chips for elem in chip]):
        return chips[0][0]*6
    hexas,result = [],[]
    for i in range(len(chips)):
        for elem in perm(chips[i]):
            hexa = [list(elem)]
            find_link(elem,chips[:i]+chips[i+1:],hexa,hexas)
    for elem in hexas:result.append([sum(x[1] for x in elem)])
    if result:return max(result)[0]
    else:return 0
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
