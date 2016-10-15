##"Fizz Buzz" est un jeu de lettres que nous allons utilisé pour enseigner la division aux robots. On va apprendre l'informatique.
##
##Vous devez écrire une fonction prenant en argument un entier positif et retournant :
##"Fizz Buzz" si le nombre est divisible par 3 et 5 ;
##"Fizz" si le nombre est divisible par 3 ;
##"Buzz" si le nombre est divisible par 5 ; 
##Le nombre en tant que chaine de caractères pour les autres cas.
##Conseils : Vous pouvez facilement résoudre cette tâche avec : if-else, l'opérateur % et les conversions de chaines de caractères.
##
##Entrée : Un nombre en tant qu'entier.
##
##Sortie : La réponse en tant que chaine de caractères.

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
