##On va apprendre aux Robots à distinguer les mots et les nombres.
##
##On vous donne une chaine de caractères avec des mots et des nombres séparés par des caractères blancs (un espace). Les mots contiennent uniquement des lettres. Vous devez vérifier si la chaine de caractères contient trois mots d'affilée. Par exemple, la chaine de caractères "start 5 one two three 7 end" contient trois mots d'affilée.
##
##Conseils : Vous pouvez résoudre facilement cette tâche avec quelques fonctions pratiques : str.split, str.isalpha et str.isdigit.
##
##Entrée : Une chaine de caractères avec des mots.
##
##Sortie : La réponse en tant que booléen.

def checkio(words):
    liste = words.split()
    count = 0
    for word in liste:
        if word.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
