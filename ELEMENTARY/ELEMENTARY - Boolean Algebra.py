##En mathématiques et en logique mathématique, l'algèbre de Boole est un sous-domaine de l'algèbre dans lequel les valeurs des variables sont "vrai" et "faux", le plus souvent notées respectivement 1 et 0. À la différence de l'algèbre élémentaire où les variables sont des nombres et les principales opérations sont l'addition et la multiplication, les principales opérations de l'algèbre de Boole sont la conjonction (notée ∧), la disjonction (notée ∨) et la négation (notée ¬).
##
##Dans cette mission, vous devez implémenter quelques opérations booléennes :
##- la conjonction (appelée ici "conjunction") notée x ∧ y, satisfait x ∧ y = 1 si x = y = 1 et x ∧ y = 0 sinon.
##- la disjonction (appelée ici "disjunction") notée x ∨ y, satisfait x ∨ y = 0 si x = y = 0 et x ∨ y = 1 sinon.
##- l'implication (implication matérielle) (appelée ici "implication") notée x→y, peut être décrite telle que ¬ x ∨ y. Si x est vrai alors la valeur de x → y est celle de y. Mais si x est faux, alors la valeur de y peut être ignorée. Cependant, cette opération doit retourner une proposition vraie et il n'y a que deux choix possibles : la valeur de retour est donc celle qui laissera l'expression la plus neutre possible, à savoir "vrai".
##- l'exclusion (ou exclusif) (appelée ici "exclusive") notée x ⊕ y, peut être décrite telle que (x ∨ y) ∧ ¬ (x ∧ y). Cette relation exclut la possibilité d'avoir simultanément les mêmes valeurs pour x et y. Définie de manière arithmétique, c'est une addition modulo 2 où 1 + 1 = 0.
##- l'équivalence (appelée ici "equivalence") notée x ≡ y peut être décrite telle que ¬ (x ⊕ y). La relation est vraie seulement si x et y ont la même valeur.
##Voici la table de vérité pour ces opérations :
##
## x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
##--------------------------------------
## 0 | 0 |  0  |  0  |  1  |  0  |  1  |
## 1 | 0 |  0  |  1  |  0  |  1  |  0  |
## 0 | 1 |  0  |  1  |  1  |  1  |  0  |
## 1 | 1 |  1  |  1  |  1  |  0  |  1  |
##--------------------------------------
##On vous donne deux valeurs booléennes x et y (1 ou 0) et un nom d'opération tel que décrit entre parenthèses ci-dessus. Vous devez calculer la valeur de la relation et la retourner avec 1 ou 0.
##
##Entrée : Trois arguments. X et Y (1 ou 0). Un nom d'opération en tant que chaine de caractères.
##
##Sortie : Le résultat (1 ou 0).

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        return not x or y
    elif operation == "exclusive":
        return ((x or y) and not (x and y))
    elif operation == "equivalence":
        return not ((x or y) and not (x and y))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
