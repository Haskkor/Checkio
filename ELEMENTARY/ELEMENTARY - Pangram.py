##Un pangramme (du grec pan : « tous » et gramma : « lettre ») est une phrase comportant toutes les lettres de l'alphabet. Avec un peu d'ingéniosité, il est facile d'en créer sur le modèle des phrases réflexives : « Jugez que ce texte renferme l'alphabet, dix voyelles, k et w. » (Thérèse Amiel).
##
##Pour Cette mission, nous utiliserons l'alphabet Latin (A-Z) qui comporte 26 lettres. Vous recevez en paramètre un texte avec des lettres de l'alphabet latin et la ponctuation. Vous devez vérifier si cette phrase est un pangramme. Les majuscules n'ont pas d'importance.
##
##Entrée: Un texte sous forme de chaine de caractères.
##
##Résultat: Si la phrase est un pangramme sous la forme d'une expression booléenne.

def check_pangram(text):
    for lettre in "abcdefghijklmnopqrstuvwxyz":
        if lettre not in text.lower():
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
