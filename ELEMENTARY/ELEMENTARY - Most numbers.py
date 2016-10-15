##On va travailler avec les nombres.
##
##On vous donne une liste de nombres (floats). Vous devez trouver la différence entre les éléments maximal et minimal. Votre fonction doit être capable de gérer un nombre indéfini d'arguments. Pour une liste d'arguments vide, la fonction doit retourner 0.
##
##Les nombres à virgule flottante (floats) sont représentés dans les ordinateurs par des fractions en base 2 (binaires). (Plus d'informations à ce propos ici). On doit vérifier le résultat avec une précision de ±0.001.
##
##Conseils : Pensez à comment travailler avec un nombre arbitraire d'arguments.
##
##Entrée : un nombre arbitraire d'arguments en tant que nombre (int, float).
##
##Sortie : La différence entre le maximum et le minimum en tant que nombre (int, float).

def checkio(*args):
    if not args:
        return 0
    else:
        min = args[0]
        max = args[0]
        for chiffre in args:
            if chiffre < min:
                min = chiffre
            if chiffre > max:
                max = chiffre
        return max - min

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
