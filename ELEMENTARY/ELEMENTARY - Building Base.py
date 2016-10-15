##La singularité est arrivé et nous sommes fait pour construire la ville-robot idéale pour nos suzerains. Dans ce Robotropolis brillant, tous les bâtiments seront rectangulaires et toutes les rues tracées sur les axes sud-nord et est-ouest des lignes dans une grille magnifique. Avant de commencer, nous devons créer une classe pour représenter le bâtiment parfait.
##
##Parce que tous les bâtiments de la ville sont rectangulaires et leurs murs sont parallèles aux rues, nous pouvons définir un bâtiment en utilisant uniquement les coordonnées du coin Sud-Ouest ainsi que deux arguments (la longueur du mur d'est en ouest, et la longueur du mur du nord au sud) ainsi que la hauteur du bâtiment. Ces valeurs sont décrits comme des nombres positifs en utilisant des unités classiques. Le point d'origine de notre système de coordonnées se situe dans le Sud-Ouest , par conséquent l'angle nord a une valeur de coordonnées supérieure à l'angle sud. Pour accomplir cette mission, nous devons utiliser quelques opérations. Voir la description des classes ci-dessous.
##
##class Building(south, west, width_WE, width_NS, height=10)
##
##Résulte en une nouvelle instance de building avec les coordonnées du coin sud-ouest à [south, west] , la tailles du bâtiment est width_WE par width_NS et la hauteur du bâtiment est height. "height" est un entier positif avec une valeur par défaut de 10.
##
## 
##>>> Building(10, 10, 1, 2, 2) 
##Building(10, 10, 1, 2, 2) 
##>>> Building(0, 0, 10.5, 2.546) 
##Building(0, 0, 10.5, 2.546, 10) 
##
##corners()
##
##Résulte un dictionnaire avec les coordonnées des coins du bâtiment. Le dictionnaire a les mots-clés suivants : "north-west", "north-east", "south-west", "south-east". Les valeurs sont des listes de Tuples avec des 2 nombres.
##
## 
##>>> Building(1, 2, 2, 2).corners() 
##{"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]} 
##
##area()
##
##Résulte en la surface du bâtiment.
##
## 
##>>> Building(1, 2.5, 4.2, 1.25).area() 
##5.25 
##
##volume()
##
##Résulte le volume du bâtiment.
##
## 
##>>> Building(1, 2.5, 4.2, 1.25, 101).volume() 
##530.25 
##
##__repr__()
##
##C'est une représentation en chaine de caractères du bâtiment. Cette méthode est utilisé pour les conversions "print" ou "str". La fonction retourne la chaine de caractères dans le format suivant: 
##"Building({south}, {west}, {width_we}, {width_ns}, {height})"
## 
##>>> str(Building(0, 0, 10.5, 2.546)) 
##"Building(0, 0, 10.5, 2.546, 10)" 
##
##Dans cette mission, toutes les données sont correctes et vous n'avez pas à implémenter des contrôles.
##
##Entrée: états et expressions avec la classe "building".
##
##Résultat: Le fonctionnement comme décris.
##
##Utilisation: Vous apprendrez ici comment écrire une classe simple avec des fonctionnalités minimum pour achever la grande gloire de Robonia.
##
##Precondition: Toutes les données sont correctes.

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {"north-west": [self.south + self.width_NS, self.west], "north-east": \
        [self.south + self.width_NS, self.west + self.width_WE], "south-west": [self.south, self.west], \
        "south-east": [self.south, self.west + self.width_WE]} 

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        return "Building(" + str(self.south) + ", " + str(self.west) + ", " + str(self.width_WE) + ", " + str(self.width_NS) + ", " + str(self.height) + ")"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
