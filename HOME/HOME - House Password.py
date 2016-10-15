##Stephan et Sophia ont oublié la sécurité et utilisent des mots de passes simples pour tout. Aide Nikola à développer un module de sécurité de mot de passes. Le mot de passe est considéré comme fort si sa longueur est supérieur ou égale à 10 symboles, il a au moins un chiffre, et doit contenir au moins une lettre majuscule et une lettre minuscule. Le mot de passe contient uniquement des lettres latines ASCII ou des chiffres.
##
##Saisie: Un mot de passe est une string (Unicode pour python 2.7).
##
##Sortie: La sortie qui indique si le mot de passe est sécurisé ou non se fera sous forme booléenne ou sous une forme qui peut être convertie et utilisée comme un booléen. Dans le résultat vous verrez le résultat converti.
##
##Example:
##checkio('A1213pokl') == False
##checkio('bAse730onE') == True
##checkio('asasasasasasasaas') == False
##checkio('QWERTYqwerty') == False
##checkio('123456123456') == False
##checkio('QwErTy911poqqqq') == True
##
##Comment cela s'utilise: Si vous êtes inquiet de la sécurité de votre application ou service, vous pouvez vérifier que les mots de passe des utilisateurs sont assez complexes. Vous pouvez utiliser ces compétences pour demander à vos utilisateurs qu'ils aient des mots passe qui on une forme spécifique (ponctuation ou unicode).
##
##Precondition:
##re.match("[a-zA-Z0-9]+", password)
##0 < len(password) ≤ 64

def containsupper(data):
    for lettre in "AZERTYUIOPQSDFGHJKLMWXCVBN":
        if lettre in data:
            return True
    return False

def containslower(data):
    for lettre in "azertyuiopqsdfghjklmwxcvbn":
        if lettre in data:
            return True
    return False

def containsnumber(data):
    for number in "0123456789":
        if number in data:
            return True
    return False

def checkio(data):
    if len(data) >= 10 and containsupper(data) and containslower(data) and containsnumber(data):
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
