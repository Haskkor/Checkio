##Quel âge avez-vous en jours ? C'est facile à calculer : soustrayez juste votre date d'anniversaire à la date d'aujourd'hui. On peut néanmoins faire de ceci un vrai challenge en comptant la différence entre n'importe quelles dates.
##
##On vous donne deux dates en tant que tuple de trois nombres - année, mois et jour. Par exemple: le 19 avril 1982 sera (1982, 4, 19). Vous devez trouver la différence, en jours, entre ces deux dates. Par exemple, entre aujourd'hui et demain = 1 jour. La différence sera toujours un nombre positif ou zéro, alors n'oubliez pas la valeur absolue.
##
##Entrée : Deux dates en tant que tuple d'entiers.
##
##Sortie : La différence entre ces deux dates en tant qu'entier.

from datetime import datetime
import math

def days_diff(date1, date2):
    duree = datetime(date1[0],date1[1],date1[2]) - datetime(date2[0],date2[1],date2[2])
    return math.fabs(duree.days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
