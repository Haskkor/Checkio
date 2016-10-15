##Pour leur entrainement en langue, nos Robots veulent en savoir plus à propos des suffixes.
##
##Dans cette tâche, on vous donne un ensemble de mots en lettres minuscules. Vérifiez s'il y a une paire de mots, telle qu'un mot soit la fin d'un autre (le suffixe d'un autre). Par exemple : {"hi", "hello", "lo"} -- "lo" est la fin de "hello", donc le résultat est True.
##
##Conseils : Pour cette tâche, vous devez connaître la manière d'itérer au travers d'un ensemble et les fonctions relatives aux chaines de caractères. Lisez en plus sur les ensembles ici et les fonctions de chaines de caractères ici.
##
##Entrée : Des mots en tant qu'ensemble de chaines de caractères.
##
##Sortie : True ou False, en tant que booléen.

def checkio(words_set):
    for word in words_set:
        for compare in words_set:
            if compare != word and word.endswith(compare):
                return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
