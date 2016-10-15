##... Si je laisse mes doigts taper au hasard sur le clavier d'une machine à écrire, il est possible qu'il en résulte une phrase compréhensible. Si une armée de singes tape sur des machines à écrire, ils pourraient écrire la totalité des livres du British Museum. La probabilité qu'ils arrivent à ce résultat est bien plus favorable que celle que les molécules retournent dans une des moitiés du récipient.
##A. S. Eddington, La Nature du Monde Physique : Conférences Gifford, 1927.
##"Ford, dit-il, il y a un nombre infini de singes à l'extérieur qui veulent nous parler du script d'Hamlet qu'ils ont élaboré."
##Douglas Adams, Le Guide du Voyageur Galactique.
##Le paradoxe du singe savant déclare qu'un singe, tapant sur une machine à écrire pendant une durée infinie, finirait par reproduire à coup sûr un texte donné, tel que les travaux complets de John Wallis, ou plus vraisemblablement, un roman de Dan Brown.
##
##Supposons que nos singes, sur leurs machines à écrire, tapent, tapent et tapent encore, jusqu'à produire un grand nombre de bouts de texte différents. Essayons de trouver si ceux-ci incluent quelques mots en particulier.
##
##On vous donne un texte pouvant inclure des mots précis. Vous devez compter combien de ces mots sont inclus dans ce texte. Un mot peut être entier ou faire partie d'un autre mot. La casse des lettres du texte n'a pas d'importance. Les mots à chercher sont donnés en minuscules et ne se répètent pas. Si un même mot apparait plusieurs fois, celui-ci ne doit être compté qu'une seule fois.
##
##Par exemple, texte - "How aresjfhdskfhskd you?", mots - ("how", "are", "you", "hello"). Le résultat est 3.
##
##Entrée : Deux arguments. Un texte en tant que chaine de caractères (en unicode pour py2) et des mots en tant qu'ensemble de chaines de caractères (en unicode pour py2).
##
##Sortie : Le nombre de mots dans le texte en tant qu'entier.

def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
