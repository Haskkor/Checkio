##Il y a plus de six ans, en Décembre 1989, je cherchais un projet de programmation "passe-temps" qui pourrait m'occuper pendant la semaine de Noël. Mon bureau (un laboratoire de recherche géré par le gouvernement à Amsterdam) serait fermé, mais j'avais un ordinateur à la maison, et pas grand-chose d'autre à faire. J'ai décidé d'écrire un interprète pour le nouveau langage auquel je réfléchissais ces derniers temps: un descendant d'ABC qui pourrait plaire aux hackers Unix / C. J'ai choisi Python comme titre de travail pour le projet, étant dans une ambiance légèrement irrévérencieuse (et un grand fan de Monty Python Flying Circus).
##Aujourd'hui, je peux dire sans hésiter que le Python a changé ma vie. J'ai déménagé sur un autre continent. Je passe mes journées de travail à développer des systèmes de grande envergure en Python, quand je ne suis pas en train de fair des modifications du Python ou de répondre à des email concernant le Python. Il ya t-shirts Python, des ateliers, des listes de diffusion, un groupe de discussion, et maintenant un livre. Franchement, mon seul désir inassouvi est d'avoir ma photo sur la première page du New York Times.
##-- Guido van Rossum, Préface de "Programming Python", Reston, VA, Mai 1996
##Cette mission est simple à résoudre. On vous donne une fonction nommée "i_love_python" qui retournera uniquement cette phrase - "I love Python!"
##
##Écrivons un essai en python qui explique pourquoi vous adorez le python (si ce n'est pas le cas, nous ferons une nouvelle mission spécialement pour les détracteurs). Publier la solution par défaut vous rapportera 0 points, le but étant de gagner des points grâce aux votes pour votre essai.
##
##Données : Non.
##
##Résultat : La chaîne de caractères (string) "I love Python!"

def i_love_python():
    print("Python is great.")
    print("I'm in a Business Intelligence course.")
    print("So boring.")
    print("Python saves my day.")
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
