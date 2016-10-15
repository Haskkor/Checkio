##On vous propose une liste d'entiers. Pour cette tache, vous devez retourner une liste qui contient seulement les éléments non uniques dans cette liste. Pour ce faire vous devez supprimer tous les éléments unique (éléments qui ne sont contenus dans la liste que une seule fois) Pendant que vous effectuez cette tâche vous ne devez pas changer l'ordre de la liste. Exemple: [1, 2, 3, 1, 3] 1 et 3 sont des éléments non uniques le résultat sera donc [1, 3, 1, 3].
##
##non-unique-elements
##
##Saisie: Une liste d'entiers.
##
##Sortie: Une liste d'entiers.

def checkio(data):
    temp = []
    for datum in data:
        if data.count(datum) != 1:
            temp.append(datum)
    return temp

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
