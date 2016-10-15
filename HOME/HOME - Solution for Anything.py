##Nous avons besoin d'une solution qui passe n'importe quel test. Le résultat de votre solution doit être valide pour n'importe quel type de comparaison avec n'importe quoi.
##
##Vous devez écrire une fonction "checkio" qui prend un argument et dont le résultat sera comparé (==, !=, etc) avec d'autres données. Le résultat de cette comparaison doit être la booléenne True.
##
##Données : Des données. Là, dans le coin, on dirait des données, ça fera l'affaire.
##
##Résultat : Ces données, mais pas les mêmes.
##
##Exemple :
##
##checkio({}) != [] # True
##checkio('Hello') < 'World' # True
##checkio(80) > 81 # True
##checkio(re) >= re # True
##checkio(re) <= math # True
##checkio(5) == ord # True
##    
##Utilisation : Cette mission vous apprendra à utiliser un peu de Python "magic".

class Dunder:
    def __init__(self,anything):
        pass
    def __lt__(self,anything):
        return True
    def __gt__(self,anything):
        return True
    def __le__(self,anything):
        return True
    def __ge__(self,anything):
        return True
    def __eq__(self,anything):
        return True
    def __ne__(self,anything):
        return True

def checkio(anything):
    return Dunder(anything)

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
