##The robots have learned that the last container which they picked up during a supply stop on another island is radioactive. There are five different kinds of spare parts contained within marked by number. The radiation is emitted from the largest group of identical spare parts (where each part is adjacently joined). Help them find this group and point out the quantity of identical parts within the group as well as the number of the spare part itself in the container.
##
##The container is represented as a square matrix. The numbers 1 through 5 are used to label the different kinds of spare parts -- the elements of the matrix. Zero is an empty cell. Find the largest group of identical numbers adjacently joined to each other and point out both the quantity of the spare parts within the group and the number of the spare part itself.
##
##Input: A square matrix as a list of lists. Each list contains integers
##
##Output: The size and marking of the largest group as a list of two integers.
##
##Example:
##
##checkio([
##    [1, 2, 3, 4, 5],
##    [1, 1, 1, 2, 3],
##    [1, 1, 1, 2, 2],
##    [1, 2, 2, 2, 1],
##    [1, 1, 1, 1, 1]]) == [14, 1]
##​
##checkio([
##    [2, 1, 2, 2, 2, 4],
##    [2, 5, 2, 2, 2, 2],
##    [2, 5, 4, 2, 2, 2],
##    [2, 5, 2, 2, 4, 2],
##    [2, 4, 2, 2, 2, 2],
##    [2, 2, 4, 4, 2, 2]]) == [19, 2]
##
##How it is used: In this task, you can learn about Union-finding algorithms and Disjoint-set data structures. It can be used in image recognition, geographic analysis and even model the partitioning of a set.
##
##Precondition:
##3 ≤ len(matrix) ≤ 10
##all(all(0 ≤ x ≤ 5 for x in row) for row in matrix
##any(any(x for x in row) for row in matrix
##The tests have only one unique solutions.

def adjacent(i,j,res):
    """ Find adjacents squares with same number. """
    for pair in res:
        if pair in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            return True
    return False

def union(res):
    """ Union lists with related items. """
    find = False
    while not find:
        find = True
        for l in res:
            for elem in l:
                for li in res:
                    if l != li and elem in li:
                        find = False
                        res.append(list(set(l) | set(li)))
                        res.remove(l)
                        res.remove(li)
                    if not find:break
            if not find:break
    return res

def checkio(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            find = False
            for r in range(len(res)):
                if matrix[i][j] == matrix[res[r][0][0]][res[r][0][1]] and \
                    adjacent(i,j,res[r]):
                        res[r].append((i,j))
                        find = True
            if not find:res.append([(i,j)])    
    res = union(res)
    j = max([[len(i),i] for i in res])
    return [j[0],matrix[j[1][0][0]][j[1][0][1]]]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
    
    assert checkio([
        [4,4,4,4,4,3,4],
        [2,3,4,4,4,4,4],
        [2,4,4,5,4,4,3],
        [4,2,2,4,1,2,4],
        [3,4,1,4,4,4,5],
        [4,4,2,4,4,2,4],
        [3,4,4,4,4,4,2]
    ]) == [15, 4], '15 of 4'
    
    assert checkio([
        [5,5,2,5,3],
        [4,2,4,5,2],
        [4,4,5,5,4],
        [2,2,5,1,3],
        [5,5,5,1,4]
    ]) == [8, 5], '8 of 5'
