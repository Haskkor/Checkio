##Essayons maintenant de trier une liste avec quelques règles spécifiques.
##
##La liste (un tuple) contient plusieurs nombres. Vous devez les trier, mais en se basant sur leurs valeurs absolues dans l'ordre croissant. Par exemple, la séquence (-20, -5, 10, 15) sera triée comme telle : (-5, 10, 15, -20). Votre fonction doit retourner la liste triée ou le tuple trié.
##
##Conseils : Vous pouvez facilement résoudre cette tâche avec ces fonctions : sorted et abs. Vous devez essayer d'utiliser le paramètre key de la fonction de tri.
##
##Précondition : Les nombres dans la liste sont uniques de part leur valeur absolue.
##
##Entrée : Un liste de nombres , un tuple..
##
##Sortie : Une liste ou un tuple (mais pas un générateur) triée en fonction des valeurs absolues dans l'ordre croissant.
##
##Complément : Les résultats de votre fonction seront affichés en tant que liste dans le volet d'explication des tests.

def checkio(numbers_array):
    return sorted(numbers_array,key=abs)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
