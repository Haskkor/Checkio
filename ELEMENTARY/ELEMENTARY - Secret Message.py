##"Où un homme sage cache-t-il une feuille ? Dans une forêt. Mais que fait-il s'il n'y a pas de forêt ? ... Il fait pousser une forêt pour la cacher dedans."
##-- Gilbert Keith Chesterton
##
##Avez-vous déjà essayé d'envoyer un message secret à quelqu'un sans utiliser les services postaux ? Vous pouvez utiliser les journaux pour parler de votre secret. Même si quelqu'un trouve votre message, c'est facile de l'envoyer balader, en disant que c'est de la paranoïa, une fausse théorie du complot. Une des manières les plus simples de cacher un message est d'utiliser les majuscules. On va trouver quelques-uns de ces messages secrets.
##
##On vous donne un texte. Rassemblez toutes les lettres majuscules en un seul mot dans leur ordre d'apparition dans le texte.
##
##Par exemple : texte = "How are you? Eh, ok. Low or Lower? Ohhh.", si on rassemble toutes les majuscules, on obtient le message "HELLO".
##
##Entrée : Un texte en tant que chaine de caractères (unicode).
##
##Sortie : Le message secret en tant que chaine de caractères ou chaine vide.

def find_message(text):
    secret = ""
    for lettre in text:
        if lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            secret += lettre
    return secret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
