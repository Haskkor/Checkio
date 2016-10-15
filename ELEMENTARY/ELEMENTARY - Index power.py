##On vous donne une liste avec des nombres positifs et un nombre N. Vous devez trouvez la N-ième puissance de l'élément de la liste à l'index N. Si N est en dehors de la liste, alors vous devez retourner -1. N'oubliez pas que le premier élément est à l'index 0.
##
##Regardons quelques exemples :
##- liste = [1, 2, 3, 4] et N = 2, alors le résultat est 32 == 9;
##- liste = [1, 2, 3] et N = 3, mais N est à l'extérieur de la liste, donc le résultat est -1.
##
##Entrée : Deux arguments. Une liste d'entiers et un nombre en tant qu'entier.
##
##Sortie : Le résultat en tant qu'entier.

def index_power(array, n):
    if n < 0 or n >= len(array):
        return -1
    else:
        return array[n] ** n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
