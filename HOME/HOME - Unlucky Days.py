##Trouvez le nombre de Vendredi 13 dans une année donnée.
##
##Input: Une année (int).
##
##Output: Nombre de "Black Friday" cette année-là (int).
##
##Exemple:
##
##checkio(2015) == 3
##checkio(1986) == 1
##
##Précondition: 1000 < |year| < 3000

import datetime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def checkio(year):
    nbr_unlucky = 0
    start_date = datetime.date(year, 1, 12)
    end_date = datetime.date(year, 12, 14)
    for single_date in daterange(start_date, end_date):
        if single_date.day == 13 and single_date.weekday() == 4:
            nbr_unlucky += 1
    return nbr_unlucky
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
