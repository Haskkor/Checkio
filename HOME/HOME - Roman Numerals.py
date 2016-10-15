##La numération romaine vient du système numérique des Romains de l'Antiquité. Elle est basée sur des lettres spécifiques de l'alphabet qui, combinées, représentent la somme (ou, dans certains cas, la différence) de leur valeur. Les dix premiers nombres romains sont :
##
##I, II, III, IV, V, VI, VII, VIII, IX et X.
##
##La numération romaine est un système décimal mais pas de position et n'inclut pas de zéro. Les nombres romains sont basés sur une combinaison de ces sept symboles :
##
##Symbole Valeur
##I 1 (unus)
##V 5 (quinque)
##X 10 (decem)
##L 50 (quinquaginta)
##C 100 (centum)
##D 500 (quingenti)
##M 1,000 (mille)
##Plus d'informations sur les chiffres romains sont disponibles sur l'article Wikipedia.
##
##Pour cette mission, vous devez retourner un nombre romain à partir d'un nombre entier donné, compris entre 1 et 3999.
##
##Données : Un nombre entier (integer).
##
##Résultat : Le nombre romain en une chaîne de caractères (string).
##
##Exemple :
##
##checkio(6) == 'VI'
##checkio(76) == 'LXXVI'
##checkio(13) == 'XIII'
##checkio(44) == 'XLIV'
##checkio(3999) == 'MMMCMXCIX'
##
##Utilisation : C'est une mission éducative qui vous laisse explorer différent systèmes de numération. Les nombres romains étant souvent utilisés en typographie, ce peut également être utilisé pour générer du texte. L'année de construction de la facade et de la pierre d'angle d'un bâtiment est souvent écrite en nombre romain. Ces nombres ont de nombreux autres usages dans le monde moderne, vous pouvez en apprendre plus ici... Ou peut-être aurez vous un Romain de l'Antiquité pour client ;)
##
##Précondition : 0 < number < 4000

def checkio(data):
    dico = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
    chaine = ""
    while data > 0:
        sup = 0
        for elem in dico.keys():
            if elem <= data and elem > sup:
                sup = elem
        chaine += dico[sup]
        data -= sup
    return chaine
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
