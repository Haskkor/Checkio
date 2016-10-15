##Une médiane est une valeur numérique qui sépare la motié supérieure d'un tableau classé de nombres de la moitié inférieure. Dans une liste ou il y a un nombre impair d'entités, la médiane est le nombre qui se trouve au milieu du tableau. Si le tableau contient un nombre pair de valeurs, il n'y a pas d'unique valeur au milieu, la mediane devient donc la moyenne des deux valeurs du milieu du tableau. Pour cette mission on vous fourni un tableau rempli de nombres naturels (N). Vous devez séparer la moitié supérieure des nombres de la moitié inférieure et trouver la médiane.
##
##Saisie: Un tableau contenant une liste d'entiers.
##
##Sortie: La médiane sous forme flottante ou entière.
##
##Exemple:
##
##checkio([1, 2, 3, 4, 5]) == 3
##checkio([3, 1, 2, 5, 3]) == 3
##checkio([1, 300, 2, 200, 1]) == 2
##checkio([3, 6, 20, 99, 10, 15]) == 12.5
##
##Comment le mettre en pratique: La médiane s'utilise en statistiques et en probabilité, elle a une valeur significatif pour les distributions faussées. Par exemple: on veut savoir la richesse moyenne des personnes d'une liste de données -- 100 personne gagnent 100$ par mois et 10 personne gagnent 1.000.000$. Si on fait une moyenne, on obtient 91.000$. Cette une valeur étrange qui ne traduit pas vraiment la réalité de la situation. Dans ce cas une médiane nous donnerait une valeur plus efficace et une meilleure image de la réalité. L'article sur Wikipedia.
##
##Precondition: 
##1 < len(data) ≤ 1000
##all(0 ≤ x < 10 ** 6 for x in data)

def checkio(data):
    temp = sorted(data)
    if len(temp) % 2 == 0:
        return (temp[len(temp) // 2] + temp[len(temp) // 2 - 1]) / 2
    else:
        return temp[len(temp) // 2]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
