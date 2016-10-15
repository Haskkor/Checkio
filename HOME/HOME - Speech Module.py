##Le module vocal de Stephen est cassé. Ce module était responsable de sa prononciation des nombres. Il doit maintenant cliquer pour entrer chaque chiffre d'un nombre, ce qui peut prendre un certain temps quand les nombres sont grands. Aide le robot à parler proprement et améliore sa vitesse de traitement des nombres en lui écrivant un nouveau module vocal. Tous les mots de la chaîne de caractères (string) doivent être séparés d'exactement un espace. Faites attention avec les espaces -- c'est difficile de remarquer qu'il y en a deux au lieu d'un.
##
##Données : Un nombre entier (integer).
##
##Résultat : Une chaîne de caractères (string) de ce nombre en toutes lettres, en anglais.
##
##Exemple :
##
##checkio(4)=='four'
##checkio(143)=='one hundred forty three'
##checkio(12)=='twelve'
##checkio(101)=='one hundred one'
##checkio(212)=='two hundred twelve'
##checkio(40)=='forty'
##
##Utilisation : Ce concept pourrait être utilisé dans un logiciel de synthèse vocale ou un système de rapports automatiques. Ce système peut aussi être utile pour écrire un robot IRC en assignant des mots ou des phrases à des valeurs numériques et en récupérant les réponses correspondant à ces valeurs.
##
##Précondition : 0 < number < 1000

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = ""
    num = str(number)
    if len(num) > 2:
        result += "{} {} ".format(FIRST_TEN[int(num[0])-1],HUNDRED)
        num = num[1:]
    if len(num) > 1:
        if int(num[0]) > 1:
            result += "{} ".format(OTHER_TENS[int(num[0])-2])
            num = num[1:]
        elif int(num[0]) > 0:
            result += "{}".format(SECOND_TEN[int(num[1])])
            num = num[2:]
        elif int(num[0]) == 0:
            num = num[1:]
    if len(num) > 0 and int(num[0]) != 0:
        result += "{}".format(FIRST_TEN[int(num[0])-1])
        
    if result[len(result)-1] == " ":
        result = result[:-1]

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

