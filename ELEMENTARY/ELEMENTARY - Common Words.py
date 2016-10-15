##Continuons à examiner les mots. On vous donne deux chaines de caratères avec des mots séparés par des virgules. Essayez de trouver ce qui est commun entre ces chaines de caractères. Les mots ne sont pas répétés au sein d'une même chaine de caractères.
##
##Votre fonction doit trouver tous les mots qui apparaissent dans les deux chaines de caractères. Le résultat doit être représenté comme une chaine de mots séparés par des virgules dans l'ordre alphabétique.
##
##Conseils : Vous pouvez facilement résoudre cette tâche avec plusieurs fonctions utiles : str.split, str.join et sorted. Essayez aussi d'utiliser le type primitif -- set.
##
##Entrée : Deux arguments en tant que chaines de caractères.
##
##Sortie : Les mots communs en tant que chaine de caractères.

def checkio(first, second):
    result = []
    firstList, secondList = first.split(","), second.split(",")
    for elem in firstList:
        if elem in secondList:
            result.append(elem)
    return ",".join(sorted(result))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
