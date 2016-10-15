##On vous donne un entier positif. Votre fonction doit calculer le produit de ses chiffres en excluant les zéros.
##
##Par exemple : Le nombre donné est 123405. Le résultat sera 1*2*3*4*5=120 (n'oubliez pas d'exclure les zéros).
##
##Conseils : Cette tâche peut être facilement résolue avec une simple conversion d'entier vers chaine de caractères et vice versa. Lisez-en plus sur les types primitifs ici.
##
##Entrée : Un entier positif.
##
##Sortie : Le produit des chiffres en tant qu'entier.

def checkio(number):
    somme = 1
    chaine = str(number)
    for nombre in chaine:
        if int(nombre) != 0:
            somme *= int(nombre)
    return somme

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
