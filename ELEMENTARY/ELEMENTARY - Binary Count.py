##Pour les Robots, le format décimal est embêtant. S'ils ont besoin de compter "1", leur cerveau électronique veut le compter en utilisant la représentation binaire de ce nombre. Vous pouvez en lire plus sur le système binaire ici.
##
##On vous donne un nombre (un entier positif). Vous devez le convertir en format binaire et compter combien d'unités (1) sont dans la représentation du nombre. Par exemple : 5 = 0b101 contient deux unités, donc la réponse est 2.
##
##Conseils : Cette tâche peut être facilement résolue avec deux fonctions -- bin et count.
##
##Entrée : Un nombre en tant qu'entier positif.
##
##Sortie : La quantité d'unités contenue dans la représentation binaire du nombre, en tant qu'entier.

def checkio(number):
    return bin(number).count("1")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
