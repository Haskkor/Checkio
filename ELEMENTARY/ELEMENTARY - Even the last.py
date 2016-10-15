##On vous donne une liste d'entiers. Vous devez trouver la somme des éléments avec des index pairs (0ème, 2ème, 4ème...) et ensuite multiplier ce total par le dernier élément de la liste. N'oubliez pas que le premier élément a un index de 0.
##
##Pour une liste vide, le résultat sera toujours 0 (zéro).
##
##Conseils : Vous pouvez facilement résoudre cette tâche avec : les index de listes, les découpages et la fonction primitive "sum".
##
##Entrée : Une liste d'entiers.
##
##Sortie : Le nombre en tant qu'entier.

def checkio(array):
    sum = 0
    if not array:
        return sum
    else:
        for i in range(0,len(array),2):
            sum += array[i]
        return sum * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
