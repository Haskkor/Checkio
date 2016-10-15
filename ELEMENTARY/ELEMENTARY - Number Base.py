##Vous rappelez-vous des bases et des systèmes de numération en classe de maths ? On va les mettre en pratique !
##
##On vous donne un nombre positif en tant que chaine de caractères, ainsi que la base qui va avec. Votre fonction doit le convertir en format décimal. La base est inférieure à 37 et supérieure à 1. La tâche utilise les chiffres et les lettres A-Z dans les chaines de caractères.
##
##Méfiez-vous des cas où le nombre ne peut pas être converti. Par exemple : "1A" ne peut pas être converti en base 9. Pour ces cas, votre fonction doit retourner -1.
##
##Conseils : Vous pouvez facilement résoudre cette tâche avec les conversions en int() et la gestion d'exceptions (Regardez à ValueError).
##
##Entrée : Deux arguments. Un nombre en tant que chaine de caractères et une base en tant qu'entier.
##
##Sortie : Le nombre converti en tant qu'entier.

def checkio(str_number, radix):
    try:
        return int(str_number,radix)
    except ValueError:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
