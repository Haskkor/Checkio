##Vous recevez une matrice de taille NxN (4≤N≤10). Vous devez vérifier si elle contient une séquence de 4 chiffres identiques alignés. Cet alignement peut être horizontal, vertical ou diagonal (diagonale NO-SE ou NE-SO).
##
##Données : Une matrice: une liste de listes d'entiers.
##
##Résultat : La présence d'un alignement en valeur booléenne (True ou False).
##
##Exemple :
##
##checkio([
##    [1, 2, 1, 1],
##    [1, 1, 4, 1],
##    [1, 3, 1, 6],
##    [1, 7, 2, 5]
##]) == True
##checkio([
##    [7, 1, 4, 1],
##    [1, 2, 5, 2],
##    [3, 4, 1, 3],
##    [1, 1, 8, 1]
##]) == False
##checkio([
##    [2, 1, 1, 6, 1],
##    [1, 3, 2, 1, 1],
##    [4, 1, 1, 3, 1],
##    [5, 5, 5, 5, 5],
##    [1, 1, 3, 1, 1]
##]) == True
##checkio([
##    [7, 1, 1, 8, 1, 1],
##    [1, 1, 7, 3, 1, 5],
##    [2, 3, 1, 2, 5, 1],
##    [1, 1, 1, 5, 1, 4],
##    [4, 6, 5, 1, 3, 1],
##    [1, 1, 9, 1, 2, 1]
##    ]) == True
##
##Utilisation : Ce concept est utile pour les jeux où il faut détecter plusieurs lignes d'éléments identiques (match 3, Puissance 4). Cet algorithme peut également servir pour la reconnaissance de formes.
##
##Précondition :
##0 ≤ len(matrix) ≤ 10
##all(all(0 < x < 10 for x in row) for row in matrix)

def checkio(mat):
    n = 4
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i+n-1 < len(mat):
                if all([mat[i][j] == mat[i+iter][j] for iter in range(1,n)]):
                    return True
            if j+n-1 < len(mat):
                if all([mat[i][j] == mat[i][j+iter] for iter in range(1,n)]):
                    return True
            if i+n-1 < len(mat) and j+n-1 < len(mat):
                if all([mat[i][j] == mat[i+iter][j+iter] \
                        for iter in range(1,n)]):
                    return True
            if i+n-1 < len(mat) and j-n+1 >= 0:
                if all([mat[i][j] == mat[i+iter][j-iter] \
                        for iter in range(1,n)]):
                    return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
